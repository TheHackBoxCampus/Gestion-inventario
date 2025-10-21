from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy import select 
from .model import mUser 
from .schema import sUser 
from auth.auth import verify_password, hash_password

async def create_user(session: AsyncSession, u: sUser): 
    user = mUser(
        username= u.username, 
        email = u.email, 
        password = hash_password(u.password)
    )
    session.add(user)
    await session.flush()
    return user


async def authenticate_user(session: AsyncSession, email: str, password: str):
    query = await session.execute(select(mUser).where(mUser.email == email))
    user = query.scalars().first() 
    if not user:
        return None
    
    if not verify_password(password, user.password): 
        return None
    return user 


