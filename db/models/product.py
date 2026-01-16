from db.base_class import Base
from sqlalchemy import Column, String, Integer, Float, Text, Boolean, DateTime
from datetime import datetime
from core.enums import Status

class Product(Base):
    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    sku_code = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String, nullable=True)
    status = Column(String, default=Status.ACTIVE.name)
    price = Column(Float, nullable=True)
    stock = Column(Integer, nullable=True)
    tax = Column(Float, nullable=True)
    owned_by = Column(Integer, nullable=True)
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    
