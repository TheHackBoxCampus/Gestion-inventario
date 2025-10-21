from typing_extensions import Annotated 
from pydantic import BaseModel, EmailStr
from pydantic.types import StringConstraints
from datetime import datetime

class sUser(BaseModel): 
    username: str
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8, max_length=16)]

class slogin(BaseModel): 
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8)]

class sUserOut(BaseModel): 
    id: int
    username: str
    email: EmailStr
    created_in: datetime 
    class Config:
        orm_mode = True
    