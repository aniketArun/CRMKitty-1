from pydantic import BaseModel, Field
from typing import Any, Optional, List
from datetime import datetime

class ShowRole(BaseModel):
    id:int
    name:str
    permissions:List[str] = Field(default_factory=list)
    description:Optional[str] = None
    created_by:Optional[int] = None
    updated_by:Optional[int] = None
    created_at:datetime = Field(default_factory= datetime.now)
    updated_at:Optional[datetime] = None
    company_id:Optional[int] = None
    class Config():
        orm_mode = True


class CreateRole(BaseModel):
    name:str
    permissions:List[str] = Field(default_factory=list)
    description:Optional[str] = None
    created_by:Optional[int] = None
    updated_by:Optional[int] = None
    created_at:datetime = Field(default_factory= datetime.now)
    updated_at:Optional[datetime] = None
    class Config():
        orm_mode = True