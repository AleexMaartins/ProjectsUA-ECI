import json
from fastapi import APIRouter, Depends, Response, UploadFile, File, BackgroundTasks
from fastapi import APIRouter, Depends, UploadFile, File, BackgroundTasks, HTTPException
from typing import Annotated, List

import pika
from services.PhotoService import PhotoService
from services.FaceRecognitionService import FaceRecognitionService
from middleware.AuthMiddleware import get_current_authenticated_user, get_optional_current_user
from services.AlbumService import AlbumService
from services.PersonService import PersonService

PhotoRouter = APIRouter(
    prefix="/photo", tags=["photo"]

)
albumService = AlbumService()

@PhotoRouter.get("/{albumId}",)
async def get_photos(albumId: str, photoService: PhotoService = Depends(), current_user: str = Depends(get_optional_current_user)):
    photos = []
    try:
        album = await albumService.get_album(albumId, current_user)
        if album['isPublic'] or current_user is not None:
            photos = await photoService.get_album_photos(current_user, albumId)
    except Exception as e: 
        print(e)
        raise HTTPException(status_code=401, detail="Not authorized to access this resource")

    return photos

@PhotoRouter.get("/person/{label}")
async def get_photos_by_person_label(label: str, photoService: PhotoService = Depends()):
    photos = []
    try:
        photos = await photoService.get_photos_by_person_label(label)
    except Exception as e:
        print(e)
    return photos

@PhotoRouter.post("/search/{albumId}")
async def search_by_photo(albumId: str, file: UploadFile = Annotated[bytes,File(...)]):
    photos = None
    photoService = PhotoService()  # Manually instantiate PhotoService
    try:
        label = await photoService.search_using_photo(albumId, file)
        if label is None:
            return None
        return await photoService.get_photos_by_person_label(label)
    except Exception as e:
        print(e)



@PhotoRouter.post("/{albumId}")
async def create_photo(
    albumId: str,
    backgroundTasks: BackgroundTasks,
    files: List[UploadFile] = File(...),
    current_user: str = Depends(get_current_authenticated_user),
    photoService: PhotoService = Depends(),
    
    faceRecognitionService: FaceRecognitionService = Depends(),
):
    if current_user is None:
        return {"error": "No user is currently logged in"}
    try:
        createdPhotos = await photoService.create_photo(current_user, albumId, files)
        # Create a connection to RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
        channel = connection.channel()

        # Declare a queue
        channel.queue_declare(queue='face_recognition')

        # Send a message to the queue
        message = json.dumps({
            'albumId': albumId,
            'imageKeyList': createdPhotos,
            'currentUser': current_user,
        })
        channel.basic_publish(exchange='', routing_key='face_recognition', body=message)

        # Close the connection
        connection.close()
    except Exception as e: 
        print(e)

    return 'ok' 


@PhotoRouter.get("/{albumId}/details/{photoId}")
async def get_photo(albumId: str, photoId: str, photoService: PhotoService = Depends(), current_user: str = Depends(get_optional_current_user), albumService: AlbumService = Depends()):
    photo = None
    try:
        album = await albumService.get_album(albumId, current_user)
        if album['isPublic'] or current_user is not None:
            photo = await photoService.get_photo(photoId)
    except Exception as e: 
        print(e)
        raise HTTPException(status_code=401, detail="Not authorized to access this resource")
    return photo

@PhotoRouter.delete("/{photoId}")
def delete_photo(
    photoId: str,
    photoService: PhotoService = Depends()
):
    personService = PersonService()
    try:
        personService.delete_faces_by_photo(photoId)
        print("1AAAAAAAAA")
        photoService.delete_photo(photoId)
    except Exception as e:
        print(e)

@PhotoRouter.get("/download/{photoId}")
async def download_photo(photoId: str, photoService: PhotoService = Depends()):
    try:
        photo_data = await photoService.get_photo_data(photoId)
        if photo_data is None:
            raise HTTPException(status_code=404, detail="Photo not found")
        return Response(content=photo_data, media_type="image/jpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to download photo") from e
