from passlib.hash import pbkdf2_sha256
from jose import jwt, JWTError 
from datetime import datetime, timedelta
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings): 
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = Field("HS256", env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: str = Field(30, env="ACCESS_TOKEN_EXPIRE_MINUTES")

settings = Settings() 

def hash_password(password: str) -> str: 
    return pbkdf2_sha256.hash(password) 

def verify_password(plain: str, hashead: str) -> bool: 
    return pbkdf2_sha256.verify(plain, hashead)

def create_access_token(data: dict): 
    to_encode = data.copy() 
    expire = datetime.utcnow() + (timedelta(minutes=float(settings.ACCESS_TOKEN_EXPIRE_MINUTES)))
    to_encode.update({'exp': expire}) 
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_access_token(token: str): 
    try: 
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]) 
        return payload
    except JWTError: 
        return None

