from db.base_class import Base
from sqlalchemy import Column, DateTime, Date, Boolean, String, Integer, Text, JSON
from core.enums import Status
from sqlalchemy.ext.mutable import MutableList
from datetime import datetime

class Report(Base):
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=True)
    title = Column(String, nullable=False)
    customer_id = Column(String, nullable=True)
    report_summary = Column(Text, nullable=True)
    test_cases = Column(MutableList.as_mutable(JSON), nullable=False)
    remarks = Column(Text, nullable=True)
    status = Column(String, default=Status.NEW.name)
    created_by = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)

