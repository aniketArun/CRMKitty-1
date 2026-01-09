from db.base_class import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, Text, DateTime
from core.enums import Status
import datetime


class Lead(Base):
    id  = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    dob = Column(Date, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    company = Column(String, nullable=True)
    source = Column(String, nullable=True)
    status = Column(String, default=Status.NEW.name)
    lead_value = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)

    refered_by=Column(Integer, nullable=True)
    created_by=Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at=Column(DateTime, nullable=True)
