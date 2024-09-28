from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_items(db: AsyncSession, model):
    query = select(model)
    result = await db.execute(query)  
    items = result.scalars().all()  
    return items