from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from modules.products.model import mProduct
from modules.products.schema import sProduct

async def stats_overview(session: AsyncSession): 
    total_products = (await session.execute(select(mProduct))).scalars().all()
    total_count = len(total_products) 
    low_stock = [p for p in total_products if p.stock <= 5]
    total_stock =  sum(p.stock for p in total_products) 
    return {"total_products": total_count, "product_low": len(low_stock), "total_stock": total_stock}