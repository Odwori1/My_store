from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict

class ProductCreate(BaseModel):
    name: str
    category: str
    cost_price: float
    sale_price: float
    quantity: int
    reorder_level: Optional[int] = 0

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    cost_price: Optional[float] = None
    sale_price: Optional[float] = None
    quantity: Optional[int] = None
    reorder_level: Optional[int] = None

class Product(ProductCreate):
    id: int

    '''class Config:
        orm_mode = True'''

    model_config = ConfigDict(from_attributes=True) 

