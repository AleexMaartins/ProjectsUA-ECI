from pydantic import BaseModel
from dotenv import load_dotenv
from supabase import create_client

import os

load_dotenv()
supabase = create_client(os.getenv("SB_URL"), os.getenv("SB_KEY"))
ENTITY = "Permissions"

class Permission(BaseModel):
    id: str | None = None
    album_id: str
    user_id: str
    role: str

class PermissionsRepository:
    ENTITY = "Permissions"

    @classmethod
    def add_permission(cls, album_id: str, user_id: str, role: str):
        response = []
        try:
            response = supabase.table(cls.ENTITY).insert(
            {
                "album_id": album_id, 
                "user_id": user_id,
                "role": role
            }).execute()
        except Exception as e: print(e)

        return response.data[0]

    @classmethod
    def get_permissions_by_album(cls, album_id: str):
        response = []
        try:
            response = supabase.table(cls.ENTITY).select('*').eq('album_id', album_id).execute()
        except Exception as e: print(e)
        return response.data
    
    @classmethod
    def remove_permission(cls, album_id: str, user_id: str):
        response = []
        try:
            response = supabase.table(cls.ENTITY).delete().eq('album_id', album_id).eq('user_id', user_id).execute()
        except Exception as e: print(e)

        return response.data