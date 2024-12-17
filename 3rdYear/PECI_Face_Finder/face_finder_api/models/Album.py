from pydantic import BaseModel
from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client
import os

load_dotenv()
supabase = create_client(os.getenv("SB_URL"), os.getenv("SB_KEY"))
ENTITY = "Album"

class Album(BaseModel):
    id: str | None = None
    god_id: str | None = None
    title: str
    description: str | None = None
    isPublic: bool
    thumbnail: str | None = None
    label: str | None = None
    creationDate: str | None = None

class AddAlbumCollaboratorReq(BaseModel):
    emails: list
    role: str

class AlbumRepository:
    def get_public_albums():
        response = []
        try:
            response = supabase.table(ENTITY).select('*').eq("isPublic", True).execute()
        except Exception as e: print(e)
        return response.data

    def create_album(album: Album, user: str):
        album.creationDate = datetime.now().isoformat()
        album.god_id = user
        response = []
        try:
            response= supabase.table(ENTITY).insert(
            {
                "title": album.title, 
                "description": album.description,
                "label": album.label, 
                "isPublic": album.isPublic, 
                "thumbnail": album.thumbnail,
                "created_at": album.creationDate, 
                "god_id": user,
            }).execute()
        except Exception as e: print(e)

        return response.data[0]

    def get_albums_by_owner(userId: str):
            response = []
            try:
                response = supabase.table(ENTITY).select("*").eq("god_id", userId).execute()
            except Exception as e: print(e)

            return response.data

    def get_album_by_id(albumId: str):
        response = []
        try:
            response = supabase.table(ENTITY).select('*').eq('id', albumId).execute()
        except Exception as e: print(e)
        return response.data[0]
    
    #TODO: start using this function to avoid repeated code
    def get_all_by_condition(arg0:str, arg1):
        response = []
        try:
            response = supabase.table(ENTITY).select('*').eq(arg0, arg1).execute()
        except Exception as e: print(e)
        return response
    
    def delete_album(albumId: str, god_id: str):
        try:
            response = supabase.table("Album").delete().filter('id', 'eq', albumId).filter('god_id', 'eq', god_id).execute()
        except Exception as e: 
            print(e)
        return response
    
    def get_albums_by_user_role(userId: str, roles: list):
        response = []
        try:
            response = supabase.table("Permissions").select("album_id").eq("user_id", userId).in_("role", roles).execute()
        except Exception as e: print(e)

        album_ids = [item['album_id'] for item in response.data]
        albums = []
        for album_id in album_ids:
            album = supabase.table(ENTITY).select("*").eq("id", album_id).execute().data[0]
            albums.append(album)
        return albums
    
    def update_thumbnail(albumId: str, thumbnail: str):
        try:
            # Ensure that the Supabase client is correctly initialized
            response = supabase.table("Album").update({"thumbnail": thumbnail}).eq("id", albumId).execute()
            print("Update Response:", response)
        except Exception as e:
            print("Error updating thumbnail:", e)
            return {"error": str(e)}
        return response