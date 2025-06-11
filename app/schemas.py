from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class CategoryEnum(str, Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UnitEnum(str, Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

class ProductCreate(BaseModel):
    name: str
    category: CategoryEnum
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: Optional[str] = None
    unit_of_measure: UnitEnum
    lead_time: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[CategoryEnum] = None
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: Optional[str] = None
    unit_of_measure: Optional[UnitEnum] = None
    lead_time: Optional[int] = None


class ProductResponse(BaseModel):
    product_id: int
    name: str
    category: CategoryEnum
    description: Optional[str]
    product_image: Optional[str]
    sku: Optional[str]
    unit_of_measure: UnitEnum
    lead_time: Optional[int]
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True

