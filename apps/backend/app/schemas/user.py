# ~/My_store/apps/backend/app/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None  # Keep your existing field
    full_name: Optional[str] = None  # New field from new schema

class UserCreate(UserBase):
    password: str  # New required field for creation

class UserUpdate(UserBase):
    password: Optional[str] = None
    is_active: Optional[bool] = None  # Keep your existing field

class UserInDBBase(UserBase):
    id: int
    is_active: bool  # Keep your existing field

    class Config:
        orm_mode = True  # Using Pydantic v1 style for compatibility

class User(UserInDBBase):
    pass

