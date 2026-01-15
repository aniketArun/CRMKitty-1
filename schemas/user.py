from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Any


class ShowUser(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    mobile: Optional[str] = None
    location: Optional[str] = None
    role: Optional[str] = None
    avatar: Optional[str] = None
    company_id:Optional[int] = None
    is_active:bool
    created_at:Any
    updated_at:Optional[Any] = None
    class Config:
        orm_mode = True

class CreateUser(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: Optional[str]=None
    email: Optional[EmailStr]=None
    mobile: Optional[str] = Field(None, pattern=r"^\+?\d{10,15}$")
    location: Optional[str]=None
    role: Optional[str]=None
    avatar: Optional[str]=None
    password:str
    class Config:
        orm_mode = True
