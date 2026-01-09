from db.base_class import Base
from core.enums import Role
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import Relationship

class User(Base):
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    mobile = Column(String, nullable=True)
    location = Column(String, nullable=True)
    role = Column(String, nullable=False, default=Role.LEAD_MANAGER.name)
    plan_id = Column(Integer, nullable=True)
    avatar = Column(String, nullable=True)
    two_factor_auth = Column(Boolean, nullable=True)
