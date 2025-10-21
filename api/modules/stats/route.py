from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_session
from .controller import stats_overview

rStats = APIRouter()

@rStats.get("/overview")
async def overview(session: AsyncSession = Depends(get_session)):
    return await stats_overview(session)



