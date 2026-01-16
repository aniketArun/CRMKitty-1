from pydantic import BaseModel, Field
from typing import Any, Optional
from core.enums import Status
from datetime import datetime

class ShowProduct(BaseModel):
    id:int
    product_name:str
    sku_code:str
    description:Optional[str] = None
    category:Optional[str] = None
    status:Optional[str] = Status.ACTIVE.name
    price:Optional[float] = None
    stock:Optional[int] = None
    tax:Optional[float] = None

    owned_by:Optional[int] = None
    created_by:Optional[int] = None
    created_at:datetime = Field(default_factory=datetime.now)
    updated_by:Optional[int] = None
    updated_at:Optional[datetime]=None

    class Config():
        orm_mode = True




class CreateProduct(BaseModel):
    product_name:str
    sku_code:str
    description:Optional[str] = None
    category:Optional[str] = None
    status:Optional[str] = Status.ACTIVE.name
    price:Optional[float] = None
    stock:Optional[int] = None
    tax:Optional[float] = None

    owned_by:Optional[int] = None
    created_by:Optional[int] = None
    created_at:datetime = Field(default_factory=datetime.now)

    updated_at:Optional[datetime]=None

    class Config():
        orm_mode = True


class UpdateProduct(BaseModel):
    product_name:Optional[str] = None
    sku_code:Optional[str] = None
    description:Optional[str] = None
    category:Optional[str] = None
    status:Optional[str] = Status.ACTIVE.name
    price:Optional[float] = None
    stock:Optional[int] = None
    tax:Optional[float] = None

    updated_at:Optional[datetime]=datetime.now

    class Config():
        orm_mode = True