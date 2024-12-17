

import datetime
import os
from dotenv import load_dotenv
from fastapi import APIRouter, Request, Depends, HTTPException
from supabase import create_client
from models.User import User, ForgotPasswordRequest, PasswordUpdate
from datetime import datetime
from fastapi.security import OAuth2PasswordBearer
from middleware.AuthMiddleware import get_user_info, get_current_user
from models.User import UserRepository
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

AuthRouter = APIRouter(
    prefix="/auth", tags=["auth"]
)

load_dotenv()
supabase = create_client(os.getenv("SB_URL"), os.getenv("SB_KEY"))

@AuthRouter.post("/sign-up")
async def create_auth_user(user: User):
    userEmail = supabase.table("User").select("email").eq("email", user.email).execute()
    if userEmail.data != []:
        return {"error": "A user with this email already exists"}
    
    credentials = {
        'email': user.email,
        'password': user.password
    }
    try:
        response = supabase.auth.sign_up(credentials)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if response.user is None:
        return {"error": "Failed to create user"}

    user_id = response.user.id
    current_time = datetime.now().isoformat()
    supabase.table("User").insert({"id": user_id, "email": user.email, "name": user.name, "created_at": current_time}).execute()

    return "User created"

@AuthRouter.post("/logout")
async def logout_user():
    result = supabase.auth.sign_out()
    return result

@AuthRouter.post("/forgot")
async def forgot_password(request: ForgotPasswordRequest):
    result = supabase.auth.reset_password_email(request.email)
    return result

@AuthRouter.post("/changePass")
async def change_password(password_update: PasswordUpdate, request: Request):
    access_token = request.headers.get('Access-Token')
    refresh_token = request.headers.get('Refresh-Token')
    supabase.auth.set_session(access_token, refresh_token)
    result = supabase.auth.update_user({"password": password_update.password})
    return result

@AuthRouter.get("/userInfo")
async def get_info(current_user: str = Depends(get_current_user)):
    if current_user is None:
        return {"error": "No user is currently logged in"}
    
    return UserRepository.get_user_by_id(current_user)