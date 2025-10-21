from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from auth.auth import create_access_token  
from auth.schema import sToken 
from .controller import create_user, authenticate_user
from .model import mUser
from .schema import sUser, sUserOut, slogin
from config.db import get_session

rUser = APIRouter(); 

# register 
@rUser.post("/register", response_model= sUserOut)
async def register(u: sUser, session: AsyncSession = Depends(get_session)): 
    print("Sd")
    query = await session.execute(sa.select(mUser).where(mUser.email == u.email))
    print(query)
    if query.scalars().first():
        raise HTTPException(status_code=400, detail='Email already registered')
    user = await create_user(session, u)
    await session.commit() 
    await session.refresh(user) 
    return user

# login 
@rUser.post("/login", response_model = sToken)
async def login(credentials: slogin, session: AsyncSession = Depends(get_session)): 
    email = credentials.email
    password = credentials.password
    user = await authenticate_user(session, email, password) 

    if not user: 
        raise HTTPException(status_code=401, detail='Invalid credentials')
    print("hola")
    access_token = create_access_token({ 'sub': str(user.id) })
    return { 'access_token': access_token, 'token_type': 'bearer'}


