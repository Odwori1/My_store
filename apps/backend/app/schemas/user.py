from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

    '''class Config:
        orm_mode = True'''

