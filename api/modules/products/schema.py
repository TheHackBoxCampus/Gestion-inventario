from pydantic import BaseModel 
from typing import Optional 
from datetime import datetime

class sProduct(BaseModel): 
    name: str
    description: Optional[str]
    stock: int 
    price: float

class sProductOut(BaseModel): 
    id: int 
    name: str
    description: Optional[str]
    stock: int 
    price: float
    created_in: datetime
    class Config: 
        orm_mode = True