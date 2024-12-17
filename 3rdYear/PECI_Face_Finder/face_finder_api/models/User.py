from pydantic import BaseModel
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()
supabase = create_client(os.getenv("SB_URL"), os.getenv("SB_KEY"))

class User(BaseModel):
    id: str | None = None
    email: str
    password: str
    name: str | None = None

class UserRepository:
    ENTITY = "User"

    @classmethod
    def get_user_by_email(cls, email: str):
        response = supabase.table(cls.ENTITY).select('*').eq('email', email).execute()
        return response.data[0] if response.data else None

    @classmethod
    def get_user_by_username(cls, username: str):
        response = supabase.table(cls.ENTITY).select('*').eq('name', username).execute()
        return response.data[0] if response.data else None
    
    @classmethod
    def get_user_by_id(cls, user_id: str):
        response = supabase.table(cls.ENTITY).select('*').eq('id', user_id).execute()
        return response.data[0] if response.data else None

    @classmethod
    def create_user(cls, user: User):
        response = supabase.table(cls.ENTITY).insert(user.dict()).execute()
        return response.data[0] if response.data else None
    
class ForgotPasswordRequest(BaseModel):
    email: str

class PasswordUpdate(BaseModel):
    password: str