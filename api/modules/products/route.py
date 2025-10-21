from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_session
from .schema import sProduct, sProductOut 
from .controller import create_products, get_products, get_product, update_product, delete_product

rProducts = APIRouter()

# create product 
@rProducts.post('', response_model=sProductOut)
async def create_product(p: sProduct, session: AsyncSession = Depends(get_session)):
    product = await create_products(session, p)
    await session.commit() 
    await session.refresh(product)
    return product 


# list all products
@rProducts.get('', response_model=list[sProductOut])
async def getProducts(limit: int = 100, session: AsyncSession = Depends(get_session)):
    products = await get_products(session, limit=limit) 
    return products


# filter product by id 
@rProducts.get('/{product_id}', response_model=sProductOut)
async def getProduct(product_id: int, session: AsyncSession = Depends(get_session)): 
    product = await get_product(session, product_id)

    if not product: 
        raise HTTPException(status_code=404, detail='Product not found!')
    
    return product 


# update product by id 
@rProducts.put('/{product_id}', response_model=sProductOut)
async def updateProduct(product_id: int, p: sProduct, session: AsyncSession = Depends(get_session)):
    product = await update_product(session, product_id, p)

    if not product:
        raise HTTPException(status_code=404, detail='Product not found!')
    
    await session.commit()
    await session.refresh(product)
    return product 


@rProducts.delete('/{product_id}', response_model=sProductOut)
async def deleteProduct(product_id: int, session: AsyncSession = Depends(get_session)):
    product = await delete_product(session, product_id)

    if not product:
        raise HTTPException(status_code=404, detail='Product not found!')
    
    await session.commit()
    return product