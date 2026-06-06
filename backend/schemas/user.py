from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from backend.models.user import UserRole

class UserBase(BaseModel):
    name:str
    email:EmailStr

class UserCreate(UserBase):
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class UserResponse(UserBase):
    id:int
    role:UserRole
    is_active:bool
    created_at:datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshTokenRequest(BaseModel):
    refresh_token: str

