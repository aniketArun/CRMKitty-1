from db.base_class import Base
from sqlalchemy import Column, String, Integer, Date, DateTime
from datetime import datetime


class FollowUp(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable= True)
    follow_date = Column(Date, nullable=False)
    lead_id = Column(Integer, nullable=True)
    customer_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    created_by = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)