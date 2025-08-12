# ~/My_store/apps/backend/app/models.py
from sqlalchemy import Column, Integer, String, Boolean, Numeric
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    cost_price = Column(Numeric, nullable=True)
    sale_price = Column(Numeric, nullable=True)
    quantity = Column(Integer, default=0)
    reorder_level = Column(Integer, default=0)

