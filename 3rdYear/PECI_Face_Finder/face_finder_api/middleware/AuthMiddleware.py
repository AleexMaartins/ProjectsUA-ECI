# AuthMiddleware.py
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from supabase import create_client
from typing import Optional
import os

load_dotenv()
supabase = create_client(os.getenv("SB_URL"), os.getenv("SB_KEY"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def optional_oauth2_scheme(request: Request):
    authorization: str = request.headers.get('Authorization')
    if authorization:
        scheme, _, token = authorization.partition(' ')
        if scheme.lower() == 'bearer':
            return token
    return None

async def get_user_info(token: str = Depends(oauth2_scheme)):
    if token is None:
        return None
    try:
        userResponse = supabase.auth.get_user(token)
        if userResponse is None:
            return None
        return userResponse.user
    except Exception as e:
        print(f"Error getting user: {e}")
        return None

async def get_current_user(token: str = Depends(oauth2_scheme)):
    if token is None:
        return None
    try:
        userResponse = supabase.auth.get_user(token)
        if userResponse is None:
            return None
        return userResponse.user.id
    except Exception as e:
        print(f"Error getting user: {e}")
        return None

async def get_current_authenticated_user(current_user: str = Depends(get_current_user)):
    if current_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No active user",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user

async def get_optional_current_user(token: Optional[str] = Depends(optional_oauth2_scheme)):
    if token is None:
        return None
    try:
        userResponse = supabase.auth.get_user(token)
        if userResponse is None:
            return None
        return userResponse.user.id
    except Exception as e:
        print(f"Error getting user: {e}")
        return None

async def get_user_roles(user_id: str):
    try:
        response = supabase.table('Permissions').select('role').eq('user_id', user_id).execute()
        if response == None:
            print("No roles found")
        return [item['role'] for item in response.data]
    except Exception as e:
        print(f"Error getting user roles: {e}")
        return []
    
async def get_user_album_roles(album_id: str, user_id: str):
    if user_id is None:
        print("No user_id provided")
        return []
    try:
        response = supabase.table('Permissions').select('role').eq('album_id', album_id).eq('user_id', user_id).execute()
        if response == None:
            print("No roles found")
        return [item['role'] for item in response.data]
    except Exception as e:
        print(f"Error getting user roles: {e}")
        return []
    
async def verify_owner(resource_id: str, resource_table: str, current_user: Optional[str]):
    response = supabase.table(resource_table).select("*").eq('id', resource_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Resource not found")

    resource = response.data[0]
    try:
        if resource['isPublic']:
            return resource
    except KeyError:
        pass

    if current_user and resource['god_id'] == current_user:
        return resource
    elif current_user is None:
        raise HTTPException(status_code=401, detail="Not authorized to access this resource")
    else:
        user_roles = await get_user_roles(current_user)
        if 'photographer' in user_roles or 'participant' in user_roles or 'admin' in user_roles:
            return resource
        else:
            raise HTTPException(status_code=401, detail="Not authorized to access this resource")