from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Any


class ShowCustomer(BaseModel):
    id:int
    first_name:str
    last_name:Optional[str] = None
    email:Optional[str] = None
    phone:Optional[str] = None
    company:Optional[str] = None
    category:Optional[str] = None
    assigned_user_id:Optional[int] = None
    addrees:Optional[str] = None
    is_active:Optional[bool] = None
    created_by:Optional[int] = None
    created_at:datetime = Field(default_factory=datetime.now)
    updated_at:Optional[datetime] = None

    class Config():
        orm_mode = True

class CreateCustomer(BaseModel):
    first_name:str = "John"
    last_name:Optional[str] = None
    email:Optional[str] = None
    phone:Optional[str] = None
    company:Optional[str] = None
    category:Optional[str] = None
    assigned_user_id:Optional[int] = None
    addrees:Optional[str] = None
    is_active:Optional[bool] = None
    created_by:Optional[int] = None
    created_at:datetime = Field(default_factory=datetime.now)
    updated_at:Optional[datetime] = None

    class Config():
        orm_mode = True

class UpdateCustomer(BaseModel):
    first_name:Optional[str] = None
    last_name:Optional[str] = None
    email:Optional[str] = None
    phone:Optional[str] = None
    company:Optional[str] = None
    category:Optional[str] = None
    assigned_user_id:Optional[int] = None
    addrees:Optional[str] = None
    is_active:Optional[bool] = None
    updated_at:Optional[datetime] = datetime.now()

    class Config():
        orm_mode = True