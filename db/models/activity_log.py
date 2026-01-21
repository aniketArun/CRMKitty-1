from db.base_class import Base
from sqlalchemy.orm import relationship
from datetime import datetime

from sqlalchemy import Column, Integer, Text, String, DateTime

class ActivityLog(Base):
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, nullable=True)
    model_id = Column(Integer, nullable=True)
    customer_id = Column(Integer, nullable=True)
    lead_id = Column(Integer, nullable=True)
    product_id = Column(Integer, nullable=True)
    role_id = Column(Integer, nullable=True)
    report_id = Column(Integer, nullable=True)
    created_by = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    follow_up_id = Column(Integer, nullable=True)
    created_by = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now)