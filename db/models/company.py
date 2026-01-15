from db.base_class import Base
from sqlalchemy import Column, Text, String, Boolean, DateTime, Integer
from datetime import datetime


class Company(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    logo = Column(String, nullable=True)
    currency  = Column(String, nullable=True)
    timezone = Column(String, nullable=True)

    billing_email = Column(String, nullable=False)
    tax_id = Column(String, nullable=False)
    billing_address = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable= True)
    updated_by = Column(Integer, nullable=True)
    plan_id = Column(Integer, nullable=True)
    license_id = Column(Integer, nullable=True)


