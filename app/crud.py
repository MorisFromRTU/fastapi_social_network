from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .database.models import User

async def get_users(db: AsyncSession):
    query = select(User)
    result = await db.execute(query)  
    users = result.scalars().all()  
    return users
    