from typing import Any, Optional, List
from pydantic import BaseModel, Field
from datetime import datetime, date
from core.enums import PaymentMethod, Status

class ShowInvoice(BaseModel):
    id:int
    company_id:Optional[int] = None
    invoice_date:date = Field(default_factory=date.today)
    customer_id:int
    due_date:date = Field(default_factory=date.today)
    discount:Optional[float] = None
    paymt_method:str = Field(default=PaymentMethod.BANK_TRANSFER.name)
    status:str = Field(default=Status.PAID.name)
    notes:Optional[str] = None
    items: List[dict] = Field(default_factory=list)


    created_by:Optional[int] = None
    created_at:datetime = Field(default_factory=datetime.now)
    updated_at:Optional[datetime] = None

    class Config():
        orm_mode = True



class CreateInvoice(BaseModel):
    company_id:Optional[int] = None
    invoice_date:date = Field(default_factory=date.today)
    customer_id:int
    due_date:date = Field(default_factory=date.today)
    discount:Optional[float] = None
    paymt_method:str = Field(default=PaymentMethod.BANK_TRANSFER.name)
    status:str = Field(default=Status.PAID.name)
    notes:Optional[str] = None
    items: List[dict] = Field(default_factory=list)


    created_by:Optional[int] = None
    created_at:datetime = Field(default_factory=datetime.now)
    updated_at:Optional[datetime] = None

    class Config():
        orm_mode = True
