from typing import Any, Optional, List
from pydantic import BaseModel, Field
from core.enums import Status
from datetime import datetime

class ShowReport(BaseModel):
    id:int
    company_id:Optional[int] = None
    title:str
    customer_id:Optional[int] = None
    report_summary:Optional[str] = None
    test_cases:List[dict] = Field(default_factory=list)
    remarks:Optional[str] = None
    status:str = Field(default_factory=Status.NEW.name)
    created_by:Optional[int]
    created_at:datetime = Field(default_factory=datetime.now)
    updated_at:Optional[datetime] = None

    class Config():
        orm_mode = True


class CreateReport(BaseModel):
    company_id:Optional[int] = None
    title:str
    customer_id:Optional[int] = None
    report_summary:Optional[str] = None
    test_cases:List[dict] = Field(default_factory=list)
    remarks:Optional[str] = None
    status:str = Field(default_factory=Status.NEW.name)
    created_by:Optional[int]
    created_at:datetime = Field(default_factory=datetime.now)
    updated_at:Optional[datetime] = None

    class Config():
        orm_mode = True
