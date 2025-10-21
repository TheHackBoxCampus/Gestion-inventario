from fastapi import FastAPI
from typing import Union 
from config.db import engine, Base
from modules.users.route import rUser
from modules.products.route import rProducts
from modules.stats.route import rStats
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(); 

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:4200'], # frontend port 
    allow_credentials=True, 
    allow_methods=['*'], 
    allow_headers=['*'],
)

# statups
@app.get("/")
def read_root():
    return {'Ok': 200 }

@app.on_event('startup')
async def startup_event(): 
    # dev enviroment
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# routes 
app.include_router(rUser, prefix="/users", tags=["users"])
app.include_router(rProducts, prefix="/products", tags=["products"])
app.include_router(rStats, prefix="/stats", tags=["stats"])




