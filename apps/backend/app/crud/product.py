from sqlalchemy.orm import Session
from app import models, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    #db_product = models.Product(**product.dict())
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(models.Product).all()

def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        return None
    #for field, value in product.dict(exclude_unset=True).items():
    for field, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, field, value)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return True

