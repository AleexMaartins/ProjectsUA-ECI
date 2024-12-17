from typing import List
import uuid
from models.Album import Album, AlbumRepository
from models.Permissions import PermissionsRepository
from models.User import UserRepository
from models.Photo import Photo, PhotoRepository
from middleware.AuthMiddleware import verify_owner, get_user_roles, get_user_album_roles
from services.PhotoService import PhotoService
from fastapi import File, HTTPException, UploadFile, status
from services.S3Service import S3Service
from PIL import Image
from io import BytesIO
class AlbumService:
    def __init__(self):
        self.photo_service = PhotoService()
        self.s3Service = S3Service()
        self.photoRepository = PhotoRepository()

    def get_public_albums(self,):
        try:
            albums = AlbumRepository.get_public_albums()
            for album in albums:
                album['ownerName'] = UserRepository.get_user_by_id(album['god_id'])['name']
                thumbnail_key = album['thumbnail']  # assuming 'thumbnail' is the key in the album object
                if not thumbnail_key:
                    continue
                thumbnail_url = self.s3Service.get_photo_url(thumbnail_key)  # get the URL for the thumbnail image
                album['thumbnail'] = thumbnail_url  # replace the thumbnail key with the URL
                
        except Exception as e:
            print(e)
        return albums

    async def get_album(self, albumId: str, user: str | None):

        # TODO: Validate if current user has access to the album

        try:
            table = "Album"
            _ = await verify_owner(albumId, table, user)
            album = AlbumRepository.get_album_by_id(albumId)
            thumbnail_key = album['thumbnail']  # assuming 'thumbnail' is the key in the album object
            thumbnail_url = self.s3Service.get_photo_url(thumbnail_key)  # get the URL for the thumbnail image
            album['thumbnail'] = thumbnail_url  # replace the thumbnail key with the URL
        except Exception as e: 
            print(e)
            raise
        return album

    def get_user_albums(self, userId: str):

        try:
            owned_albums = AlbumRepository.get_albums_by_owner(userId)
            other_albums = AlbumRepository.get_albums_by_user_role(userId, ['photographer', 'participant','admin'])
        except Exception as e:
            print(e)
            return []

        for album in owned_albums + other_albums:
            thumbnail_key = album['thumbnail']  # assuming 'thumbnail' is the key in the album object
            if not thumbnail_key:
                continue
            thumbnail_url = self.s3Service.get_photo_url(thumbnail_key)  # get the URL for the thumbnail image
            album['thumbnail'] = thumbnail_url  # replace the thumbnail key with the URL
            
        return owned_albums + other_albums

    async def create_album(album: Album, user: str):
        try:
            if not album.thumbnail:
                album.thumbnail = "default_album_thumbnail/f6ac1b1b-1f88-4d73-ad62-bcd5b9f61b71.webp"
            newAlbum = AlbumRepository.create_album(album, user)
            return newAlbum
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="An error occurred while creating the album.")

    async def delete_album(self, albumId: str, user: str):
        try:
            await self.photo_service.delete_all_album_photos(albumId)
            AlbumRepository.delete_album(albumId, user)
        except Exception as e:
            print(e)

    async def add_user_to_album(self, albumId: str, emails: list, role: str, current_user: str):
        try:
            user_roles = await get_user_roles(current_user)
            if 'admin' not in user_roles:
                await verify_owner(albumId, "Album", current_user)
                if 'photographer' in user_roles or 'participant' in user_roles:
                        raise HTTPException(status_code=403, detail="Not authorized to modify this album")
        except Exception as e:
            raise HTTPException(status_code=403, detail="Not authorized to modify this album")

        for userEmail in emails:
            user_to_add = UserRepository.get_user_by_email(userEmail)
            if user_to_add is None:
                raise HTTPException(status_code=404, detail="User not found")

            existing_permissions = PermissionsRepository.get_permissions_by_album(albumId)
            if any(permission['user_id'] == user_to_add['id'] for permission in existing_permissions):
                raise HTTPException(status_code=400, detail="User already has a permission for this album")

            try:
                PermissionsRepository.add_permission(albumId, user_to_add['id'], role)
            except Exception as e:
                raise HTTPException(status_code=500, detail="Failed to add user to album")
            
        return {"message": "User added to album successfully"}
    
    async def get_album_permissions(self, albumId: str):
        try:
            permissions = PermissionsRepository.get_permissions_by_album(albumId)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Failed to fetch permissions")

        users_with_permissions = []
        for permission in permissions:
            user = UserRepository.get_user_by_id(permission['user_id'])
            if user is not None:
                users_with_permissions.append({
                    'user_name': user['name'], 
                    'role': permission['role']
                })

        return users_with_permissions

    async def remove_user_from_album(self, albumId: str, username: str, current_user: str):
        try:
            user_roles = await get_user_roles(current_user)
            if 'admin' not in user_roles:
                await verify_owner(albumId, "Album", current_user)
        except Exception as e:
            raise HTTPException(status_code=403, detail="Not authorized to modify this album")

        user_to_remove = UserRepository.get_user_by_username(username)
        if user_to_remove is None:
            raise HTTPException(status_code=404, detail="User not found")

        try:
            PermissionsRepository.remove_permission(albumId, user_to_remove['id'])
        except Exception as e:
            raise HTTPException(status_code=500, detail="Failed to remove user from album")

        return {"message": "User removed from album successfully"}
    
    async def check_user_upload(self, album_id: str, current_user: str):
        album = await verify_owner(album_id, 'Album', current_user)
        user_roles = await get_user_album_roles(album_id, current_user)
        if album and album['god_id'] == current_user or any(role in user_roles for role in ['photographer', 'admin']):
            return {"message": "User has necessary permissions"}
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User does not have the necessary permissions")
        
    async def check_user_settings(self, album_id: str, current_user: str):
        album = await verify_owner(album_id, 'Album', current_user)
        user_roles = await get_user_album_roles(album_id, current_user)
        if album and album['god_id'] == current_user or any(role in user_roles for role in ['admin']):
            return {"message": "User has necessary permissions"}
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User does not have the necessary permissions")
        
    async def update_thumbnail(self, album_id: str, photo_key: str):
        AlbumRepository.update_thumbnail(album_id, photo_key)
        return {"message": "entered service"}

    async def create_thumbnail(
        self,
        userId: str,
        albumId: str,
        files: List[UploadFile],
    ):
        album_owner = await verify_owner(albumId, 'Album', userId)
        user_roles = await get_user_roles(userId)
        if 'photographer' not in user_roles and 'admin' not in user_roles and userId != album_owner['god_id']:
            raise HTTPException(status_code=401, detail="Not authorized to create photo in this album")

        try:
            photos_keys = []
            for file in files:
                fileBytes = await file.read()

                # Convert image to WebP format
                image = Image.open(BytesIO(fileBytes))
                webp_image = BytesIO()
                image.save(webp_image, format="webp")
                webp_image.seek(0)
                

                fileName = f"{uuid.uuid1()}.webp"
                fileKey = f"{userId}/{albumId}/album_thumbnail/{fileName}"
                photo = Photo(
                    album_id=albumId,
                    uploader_id=userId,
                    image_key=fileKey,
                    thumbnail=""  # TODO: Generate thumb key if needed
                )
               
                self.s3Service.delete_thumbs(userId, albumId)
                self.s3Service.upload_image(fileKey, webp_image.getvalue())
                photos_keys.append(fileKey)
        except Exception as e:
            print("Exception in photo creation:", e)
            raise

        return photos_keys