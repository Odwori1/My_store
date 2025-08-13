# ~/My_store/apps/backend/app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from decimal import Decimal

# ---------- User Schemas ----------
class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    is_active: bool = True

class UserCreate(UserBase):
    password: str  # Only for creation

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# ---------- Product Schemas ----------
class ProductBase(BaseModel):
    name: str
    category: Optional[str] = None
    cost_price: Optional[Decimal] = None
    sale_price: Optional[Decimal] = None
    quantity: int = 0
    reorder_level: int = 0

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


# ---------- TestTable Schemas ----------
class TestTableBase(BaseModel):
    name: str

class TestTableCreate(TestTableBase):
    pass

class TestTable(TestTableBase):
    id: int

    class Config:
        orm_mode = True

