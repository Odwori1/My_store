from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.get("/", response_model=list[schemas.Product])
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@router.put("/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    return crud.update_product(db, product_id, product)

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    crud.delete_product(db, product_id)
    return {"detail": "Product deleted"}

