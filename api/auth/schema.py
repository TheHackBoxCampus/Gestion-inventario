from pydantic import BaseModel

class sToken(BaseModel): 
    access_token: str
    token_type: str = 'bearer'


