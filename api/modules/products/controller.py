from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy import select 
from .model import mProduct
from .schema import sProduct

async def create_products (session: AsyncSession, p: sProduct):
    product = mProduct(**p.model_dump())
    session.add(product)
    await session.flush()
    return product 


async def get_products (session: AsyncSession, limit: int = 100, offset: int = 0):
    query = await session.execute(select(mProduct).limit(limit).offset(offset))
    return query.scalars().all()


async def get_product(session: AsyncSession, product_id: int): 
    return await session.get(mProduct, product_id)


async def update_product(session: AsyncSession, product_id: int, p: sProduct): 
    product = await session.get(mProduct, product_id)
    if not product:
        return None
    
    for key, value in p.model_dump().items():
        setattr(product, key, value)
    
    session.add(product)
    await session.flush()
    return product
    
async def delete_product(session: AsyncSession, product_id: int): 
    product = await session.get(mProduct, product_id)
    if not product:
        return None
    
    await session.delete(product)
    await session.flush()
    return product
    