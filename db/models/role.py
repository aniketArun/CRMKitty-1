from db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer, JSON, Text
from sqlalchemy.ext.mutable import MutableList
from datetime import datetime

class Role(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(MutableList.as_mutable(JSON), nullable=False, default=list)
    description = Column(Text, nullable = False)
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, nullable=True)
    company_id = Column(Integer, nullable=True)

