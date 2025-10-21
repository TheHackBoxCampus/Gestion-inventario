from sqlalchemy import Integer, Column, String, Text, DateTime, Numeric
from sqlalchemy.sql import func as sqlfunc 
from config.db import Base

class mProduct(Base): 
    __tablename__ = 'products'; 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False, index=True)
    description = Column(Text)
    stock = Column(Integer, nullable=False, default=0)
    price = Column(Numeric(12,2))
    created_in = Column(DateTime(timezone=True), server_default=sqlfunc.now())