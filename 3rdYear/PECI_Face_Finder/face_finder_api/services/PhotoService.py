import uuid
from fastapi import Depends, File, HTTPException
from middleware.AuthMiddleware import get_user_roles, verify_owner
from services.S3Service import S3Service
from models.Photo import Photo, PhotoRepository
from services.FaceRecognitionService import FaceRecognitionService
from models.Person import PersonRepository
import os
from PIL import Image
import numpy as np

class PhotoService:
    def __init__(
        self,
        # s3Service: S3Service = Depends(),
        # photoRepository: PhotoRepository = Depends(),
    ):
        self.photoRepository = PhotoRepository()
        self.s3Service = S3Service()
        self.personRepository = PersonRepository()
        self.faceRecognitionService = FaceRecognitionService()

    async def get_album_photos(self, currentUser, albumId):
    # Validate if the current user has read access to the album
        try:
            _ = await verify_owner(albumId, "Album", currentUser)
            photos = self.photoRepository.get_photos(albumId)
            for photo in photos:
                url = self.s3Service.get_photo_url(photo['image_key'])
                photo['image_key'] = url
        except Exception as e:
            print(e)
            raise

        return photos

    async def get_photos_by_person_label(self, label):
        photos = []
        try:
            photos = self.photoRepository.get_photos_by_person_label(label)
            for photo in photos:
                url = self.s3Service.get_photo_url(photo['photo_imagekey'])
                photo['image_key'] = url
        except Exception as e:
            print(e)
        return photos
        
    async def search_using_photo(self,albumId, image: File):
        masterDirName = self.faceRecognitionService.temporary_directories()
        await self.faceRecognitionService.get_person_and_face(albumId, masterDirName) 
        im = Image.open(image.file)
        image = np.asarray(im)
        await self.faceRecognitionService.store_faces(image, masterDirName) 
        for face in os.scandir(masterDirName + os.getenv("FACES")):  # match faces to persons
            label = await self.faceRecognitionService.run_search_face(face, masterDirName)
        await self.faceRecognitionService.delete_temporary_directories(masterDirName)
        if label is None:
            return None
        return label

    
    async def create_photo(
        self,
        userId: str,
        albumId: str,
        files: list[File],
    ):
        album_owner = await verify_owner(albumId, 'Album', userId)
        user_roles = await get_user_roles(userId)
        if 'photographer' not in user_roles and 'admin' not in user_roles and userId != album_owner['god_id']:
            raise HTTPException(status_code=401, detail="Not authorized to create photo in this album")
        try:
            photos_keys = []
            for file in files:
                fileBytes = await file.read()
                fileName = str(uuid.uuid1())+ ".jpg"
                fileKey = f"{userId}/{albumId}/photos/{fileName}"
                photo = Photo(
                    album_id=albumId,
                    uploader_id=userId,
                    image_key=fileKey,
                    thumbnail=""  # TODO: Generate thumb key
                )
                self.photoRepository.upload_photo(photo)
                self.s3Service.upload_image(fileKey, fileBytes)
                photos_keys.append(fileKey)
        except Exception as e:
            print("Exception in photo creation:", e)
            raise
        return photos_keys

    def delete_photo(self, photoId: str):
        print ("DELETE PHOTOAAAAAAAAAAAAAAAAA", photoId)

        try:
            photo = self.photoRepository.get_photo(photoId)
            self.photoRepository.delete_photo(photoId)
            self.s3Service.delete_image(photo[0]['image_key'])
        except Exception as e:
            print(e)

    async def delete_all_album_photos(self, albumId: str):
        try:
            photos = self.photoRepository.get_photos(albumId)
            for photo in photos:
                self.photoRepository.delete_face(photo['image_key'])
                self.photoRepository.delete_photo(photo['id'])
                self.s3Service.delete_image(photo['image_key'])
        except Exception as e:
            print(e)

    async def get_photo_data(self, photoId: str):
        try:
            photo = self.photoRepository.get_photo(photoId)
            if not photo:
                return None
            image_key = photo[0]['image_key']
            photo_data = self.s3Service.download_image(image_key)
            
            return photo_data
        except Exception as e:
            print(e)
            raise
    async def get_photo(self, photoId: str):
        try:
            photo = self.photoRepository.get_photo(photoId)
            if photo:
                photo = photo[0]  # get the first photo from the list
                url = self.s3Service.get_photo_url(photo['image_key'])
                photo['image_key'] = url
        except Exception as e:
            print(e)
        return photo
