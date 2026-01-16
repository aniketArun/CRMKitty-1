from sqlalchemy import Column, Integer, Float, JSON, Text, Boolean, String, Date, DateTime
from sqlalchemy.ext.mutable import MutableList
from db.base_class import Base
from datetime import datetime, date
from core.enums import Status, PaymentMethod


class Invoice(Base):
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer,nullable=True)
    invoice_date = Column(Date, default=date.today)
    customer_id = Column(Integer, nullable=False)
    due_date = Column(Date, default=date.today)
    discount = Column(Float, nullable=True)
    paymt_method = Column(String, default=PaymentMethod.BANK_TRANSFER.name)
    status = Column(String, default=Status.PAID.name)
    notes = Column(Text, nullable=True)
    items = Column(MutableList.as_mutable(JSON), nullable=False)

    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    created_at = Column(DateTime, default= datetime.now)
    updated_at = Column(DateTime, nullable=True)
