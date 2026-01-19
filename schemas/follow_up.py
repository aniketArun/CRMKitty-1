from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

class CreateFollowUp(BaseModel):
    title : str = Field(default="Follow-up on Legal Complience")
    description :Optional[str] = None
    follow_date :date = Field(default=date.today)
    lead_id :Optional[int] = None
    customer_id :Optional[int] = None
    user_id :Optional[int] = None

    class Config():
        orm_mode = True

class ShowFollowUp(BaseModel):
    id :int
    title : str
    description :Optional[str] = None
    follow_date :date = Field(default=date.today)
    lead_id :Optional[int] = None
    customer_id :Optional[int] = None
    user_id :Optional[int] = None
    created_by :Optional[int] = None
    created_at :Optional[datetime] = Field(default_factory=datetime.now)
    updated_at :Optional[datetime] = None

    class Config():
        orm_mode = True

class UpdateFollowUp(BaseModel):
    title : Optional[str] = None
    description :Optional[str] = None
    follow_date :Optional[date] = Field(default=date.today)
    lead_id :Optional[int] = None
    customer_id :Optional[int] = None
    user_id :Optional[int] = None

    class Config():
        orm_mode = True

