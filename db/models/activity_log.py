from db.base_class import Base
from sqlalchemy.orm import relationship
from datetime import datetime

from sqlalchemy import Column, Integer, Text, String, DateTime

class ActivityLog(Base):
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    user_id = Column(Integer, nullable=True)
    model_id = Column(Integer, nullable=True)