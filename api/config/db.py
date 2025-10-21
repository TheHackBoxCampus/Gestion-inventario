from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import Field

class Settings(BaseSettings): 
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

settings = Settings(); 

engine = create_async_engine(
    settings.DATABASE_URL, 
    future=True, 
    echo=False, 
    pool_size=10, 
    max_overflow=20
)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

async def get_session():
    async with AsyncSessionLocal() as session: 
        yield session 


