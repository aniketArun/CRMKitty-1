from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

class Customer(Base):
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable = True)
    company = Column(String, nullable=True)
    category = Column(String, nullable=True)
    assigned_user_id = Column(Integer, nullable=True)
    addrees = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_by = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    