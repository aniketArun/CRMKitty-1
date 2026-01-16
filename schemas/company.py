from typing import Any, Optional
from datetime import datetime
from  pydantic import BaseModel, Field


class CreateCompany(BaseModel):
    name:str
    email:Optional[str] = None
    phone:Optional[str] = None
    logo:Optional[str] = None
    currency:Optional[str] = None
    timezone:Optional[str] = None

    billing_email:str
    tax_id:str
    billing_address:Optional[str] = None

    created_at:datetime = Field(default_factory=datetime.now)
    updated_at:Optional[datetime] = None
    updated_by:Optional[int] = None
    plan_id:Optional[int] = None
    license_id:Optional[int] = None

    class Config():
        orm_mode = True


class ShowCompany(BaseModel):
    id:int
    name:str
    email:Optional[str] = None
    phone:Optional[str] = None
    logo:Optional[str] = None
    currency:Optional[str] = None
    timezone:Optional[str] = None

    billing_email:str
    tax_id:str
    billing_address:Optional[str] = None

    created_at:datetime = Field(default_factory=datetime.now)
    updated_at:Optional[datetime] = None
    updated_by:Optional[int] = None
    plan_id:Optional[int] = None
    license_id:Optional[int] = None

    class Config():
        orm_mode = True


class UpdateCompany(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    logo: Optional[str] = None
    currency: Optional[str] = None
    timezone: Optional[str] = None
    billing_email: Optional[str] = None
    tax_id: Optional[str] = None
    billing_address: Optional[str] = None
    plan_id: Optional[int] = None
    license_id: Optional[int] = None

    class Config():
        orm_mode = True
