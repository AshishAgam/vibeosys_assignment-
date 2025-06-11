from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import ProductResponse, ProductCreate, ProductUpdate
from app.crud import get_products, get_product_by_id, create_product, perform_update_product


router = APIRouter(prefix="/product", tags=["product"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/product/list", response_model=List[ProductResponse])
def list_products(skip: int = 0, db: Session = Depends(get_db)):
    return get_products(db, skip=skip)

@router.get("/product/{pid}/info", response_model=ProductResponse)
def get_product_info(pid: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/product/add", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.put("/product/{pid}/update", response_model=ProductResponse)
def update_product(pid: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated = perform_update_product(db, pid, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated