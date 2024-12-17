from typing import List
from fastapi import APIRouter, Depends, File, HTTPException, Request, UploadFile
from models.Album import Album, AddAlbumCollaboratorReq
from models.Permissions import Permission
from services.AlbumService import AlbumService
from middleware.AuthMiddleware import get_current_authenticated_user, get_optional_current_user, verify_owner
AlbumRouter = APIRouter(
    prefix="/albums", tags=["album"]
)

@AlbumRouter.get("/", )
async def index():
    publicAlbums = []
    try:
        album_service = AlbumService()
        publicAlbums = album_service.get_public_albums()
    except Exception as e: print(e)

    return publicAlbums

@AlbumRouter.get("/user", )
async def get_user_albums(current_user: str = Depends(get_current_authenticated_user)):
    if current_user is None:
        return {"error": "User not found"}
    album_service = AlbumService()
    return album_service.get_user_albums(current_user)

@AlbumRouter.get("/{album_id}", response_model=Album)
async def get_album(album_id: str, current_user: str = Depends(get_optional_current_user)):
    album_service = AlbumService()
    return await album_service.get_album(album_id, current_user)

@AlbumRouter.post("/", response_model=Album)
async def create_album(album: Album, current_user: str = Depends(get_current_authenticated_user)):
    if current_user is None:
        return {"error": "No user is currently logged in"}
    return await AlbumService.create_album(album, current_user)

@AlbumRouter.delete("/{albumId}")
async def delete_album(albumId: str, current_user: str = Depends(get_current_authenticated_user)):
    try:
        album_service = AlbumService()  
        await album_service.delete_album(albumId, current_user)
    except Exception as e: print(e)

@AlbumRouter.get("/{albumId}/permissions")
async def get_album_permissions(
    albumId: str, 
    current_user: str = Depends(get_current_authenticated_user),
    album_service: AlbumService = Depends()
):
    return await album_service.get_album_permissions(albumId)

@AlbumRouter.post("/{albumId}/permissions")
async def add_user_to_album(
    albumId: str, 
    reqData: Request,
    current_user: str = Depends(get_current_authenticated_user),
    album_service: AlbumService = Depends()
):
    data = await reqData.json()
    return await album_service.add_user_to_album(albumId, data["emails"], data["role"], current_user)

@AlbumRouter.delete("/{albumId}/permissions")
async def remove_user_from_album(
    albumId: str, 
    username: str, 
    current_user: str = Depends(get_current_authenticated_user),
    album_service: AlbumService = Depends()
):
    return await album_service.remove_user_from_album(albumId, username, current_user)

@AlbumRouter.get("/upload/{album_id}")
async def check_upload_permissions(
    album_id: str, 
    current_user: str = Depends(get_optional_current_user),
    album_service: AlbumService = Depends()
):

    return await album_service.check_user_upload(album_id, current_user)

@AlbumRouter.get("/settings/{album_id}")
async def check_settings_permissions(
    album_id: str, 
    current_user: str = Depends(get_optional_current_user),
    album_service: AlbumService = Depends()
):

    return await album_service.check_user_settings(album_id, current_user)

@AlbumRouter.put("/{album_id}/thumbnail")
async def update_album_thumbnail(
    album_id: str, 
    thumbnail: List[UploadFile] = File(...),
    current_user: str = Depends(get_current_authenticated_user),
    album_service: AlbumService = Depends()
):
    try:
        thumbnail_key = await album_service.create_thumbnail(current_user, album_id, thumbnail)
        if thumbnail_key:
            update_response = await album_service.update_thumbnail(album_id, thumbnail_key[0])
            if "error" in update_response:
                raise HTTPException(status_code=500, detail="Failed to update thumbnail")
            return {"message": "Thumbnail updated successfully", "thumbnail_key": thumbnail_key}
        else:
            raise HTTPException(status_code=400, detail="Thumbnail key is empty")
    except Exception as e:
        print("Error in update_album_thumbnail:", e)
        raise HTTPException(status_code=500, detail=str(e))
