from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, deps

router = APIRouter()

@router.get("/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(deps.get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(deps.get_db)):
    return crud.create_product(db, product)

