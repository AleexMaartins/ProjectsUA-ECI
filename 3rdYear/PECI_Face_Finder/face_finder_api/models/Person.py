from pydantic import BaseModel
from dotenv import load_dotenv
from supabase import create_client
import os
import requests

load_dotenv()
supabase = create_client(os.getenv("SB_URL"), os.getenv("SB_KEY"))


class Person(BaseModel):
    id: str | None = None
    album_id: str
    uploader_id: str
    image_key: str
    thumbnail: str
    
class Faces(BaseModel):
    id: str | None = None
    photo_imagekey: str
    zoomed_face: str
    depth: str | None
    person_label: str | None

class EditPerson(BaseModel):
    newLabel: str
    oldLabel: str

class PersonRepository:
    def get_people(self, albumId: str):
        response = supabase.table("Person").select('thumbnail_key','label','is_named').eq('album_id',albumId).execute()
        return response.data

    def get_person(self, label: str):
        response = supabase.table("Person").select('thumbnail_key','label','is_named').eq('label',label).execute()
        if len(response.data) == 0:
            print("No person found")
            return 
        print ("aqui estou mais um dia sorbre")
        return response.data[0] 
    
    def set_label(self, newLabel:str, oldLabel:str):
        # supabase.table("Faces").update({"person_label": None}).eq("person_label", oldLabel).execute()
        supabase.table("Person").update({"label": newLabel, "is_named": True}).eq("label", oldLabel).execute()
        # supabase.table("Faces").update({"person_label": newLabel}).eq("person_label", None).execute()
        return ""  
    
    def get_faces_by_photo(self, photoId: str):
        photo_imagekey = supabase.table("Photo").select('image_key').eq('id',photoId).execute().data[0]['image_key']
        faces = supabase.table("Faces").select('*').eq('photo_imagekey',photo_imagekey).execute()
        return faces.data
    
    async def delete_face(self, photoId: str):
        supabase.table("Faces").delete().eq('photo_imagekey', photoId).execute()
        return ""

    async def get_labels(self, faceId: str):
        label = supabase.table("Faces").select('person_label').eq('id',faceId).execute()
        return label.data[0]['person_label']
    
    async def delete_person(self, label: str):
        supabase.table("Person").delete().eq('label', label).execute()
        return ""
    
    async def get_faces_by_person(self, label: str):
        faces = supabase.table("Faces").select('*').eq('person_label',label).execute()
        return faces.data