from sqlalchemy.orm import Session
from app.models import ProductModel
from app.schemas import ProductCreate, ProductUpdate

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ProductModel).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(ProductModel).filter(ProductModel.product_id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def perform_update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = get_product_by_id(db, product_id)
    if not db_product:
        return None
    update_data = product.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_product, field, value)

    db.commit()
    db.refresh(db_product)
    return db_product
