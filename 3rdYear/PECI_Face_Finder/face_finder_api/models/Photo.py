from pydantic import BaseModel
from dotenv import load_dotenv
from supabase import create_client
import os

load_dotenv()
supabase = create_client(os.getenv("SB_URL"), os.getenv("SB_KEY"))


class Photo(BaseModel):
    id: str | None = None
    album_id: str
    uploader_id: str
    image_key: str
    thumbnail: str

class PhotoRepository:
    def get_photos(self, albumId: str):
        response = []
        try:
            response = supabase.table("Photo").select('*').eq('album_id', albumId).execute()
        except Exception as e: print(e)
        return response.data

    def upload_photo(self, photo: Photo):
        try:
            supabase.table("Photo").insert(
                    {
                        "album_id": photo.album_id, 
                        "uploader_id": photo.uploader_id, 
                        "image_key": photo.image_key, 
                        "thumbnail": photo.thumbnail,
                    }
                ).execute()
        except Exception as e: print(e)

    def get_photo(self, photoId: str):
        response = supabase.table("Photo").select('image_key').eq('id', photoId).execute()
        return response.data
    
    def delete_photo(self, photoId: str):
        supabase.table("Photo").delete().eq('id', photoId).execute()
        return ""
    
    def get_photos_by_person_label(self, label: str):
        peopleKeys = []
        try:
            peopleKeys = supabase.table("Faces").select('photo_imagekey').eq('person_label', label).execute()
        except Exception as e: print(e)
        return peopleKeys.data
    
