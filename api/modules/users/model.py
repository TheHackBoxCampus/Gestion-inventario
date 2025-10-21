from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.sql import func as sqlfunc 
from config.db import Base

class mUser(Base): 
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), nullable=False)
    email = Column(String(256), unique=True, nullable=False, index=True) 
    password = Column(String(16), nullable=False)
    created_in = Column(DateTime(timezone=True), nullable=False, server_default=sqlfunc.now())

