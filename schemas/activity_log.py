from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ActivityLog(BaseModel):
    id:int
    description:str
    user_id:Optional[int] = None
    model_id: Optional[int] = None
    customer_id:Optional[int] = None
    lead_id:Optional[int] = None
    product_id:Optional[int] = None
    role_id:Optional[int] = None
    report_id:Optional[int] = None
    created_by :Optional[int] = None
    company_id:Optional[int] = None
    follow_up_id:Optional[int] = None
    created_at:datetime = Field(default=datetime.now)

    class Config():
        orm_mode = True
