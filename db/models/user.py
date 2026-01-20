from db.base_class import Base
# from core.enums import Role
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.models.role import Role

class User(Base):
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    mobile = Column(String, nullable=True)
    location = Column(String, nullable=True)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False) 
    role = relationship("Role", backref="users") # <-- link to Role
    avatar = Column(String, nullable=True)
    two_factor_auth = Column(Boolean, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    password = Column(String, nullable=True)
    company_id = Column(Integer, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
