from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime

class ShowLead(BaseModel):
    id: int
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    dob: Optional[date] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, pattern=r"^\+?\d{10,15}$")
    company: Optional[str] = None
    source: Optional[str] = None
    status: Optional[str] = Field("NEW")  # default value
    lead_value: Optional[float] = None
    notes: Optional[str] = None

    refered_by: Optional[int] = None
    created_by: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    updated_by:Optional[int] = None
    class Config:
        orm_mode = True

class CreateLead(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    dob: Optional[date] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, pattern=r"^\+?\d{10,15}$")
    company: Optional[str] = None
    source: Optional[str] = None
    status: Optional[str] = None
    lead_value: Optional[float] = None
    notes: Optional[str] = None

    refered_by: Optional[int] = None
    created_by: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class UpdateLead(BaseModel):
    first_name: Optional[str] = Field(None, min_length=1, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    dob: Optional[date] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, pattern=r"^\+?\d{10,15}$")
    company: Optional[str] = None
    source: Optional[str] = None
    status: Optional[str] = None
    lead_value: Optional[float] = None
    notes: Optional[str] = None

    refered_by: Optional[int] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True