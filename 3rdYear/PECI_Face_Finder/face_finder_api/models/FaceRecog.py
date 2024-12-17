from dotenv import load_dotenv
from supabase import create_client
import os

load_dotenv()
supabase = create_client(os.getenv("SB_URL"), os.getenv("SB_KEY"))


class FaceRecogRepository:

    def supabase_create_person(self, label, albumId):  # works
        supabase.table("Person").insert(
        {
            "label": label,
            "is_named": False,
            "album_id": albumId,
        }).execute()

    def supabase_create_face(self, photoKey, personLabel, faceKey):
        supabase.table("Faces").insert(
        {
            "photo_imagekey": photoKey,
            "zoomed_face": faceKey,
            "depth": 0,
            "person_label": personLabel
        }).execute()

    def supabase_update_person_thumbnail(self, personLabel, thumbnailKey):
        supabase.table("Person").update({"thumbnail_key": thumbnailKey}).eq(
            "label", personLabel).execute()

    def supabase_get_person_and_face(self, albumId):
        try:
            return supabase.table("Person").select("label, is_named, Faces (*)").filter('album_id','eq',albumId).execute()
        except Exception as e:
            print(e)
            return []
