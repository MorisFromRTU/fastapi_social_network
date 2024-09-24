from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import database


async def get_users(db: AsyncSession) -> list:
    query = select(database.models.User)
    result = await db.execute(query)  
    users = result.scalars().all()  
    return users

async def get_user(db: AsyncSession, username: str) -> database.models.User:
    query = select(database.models.User).filter(database.models.User.username == username)
    result = await db.execute(query)
    existing_user = result.scalars().first()
    return existing_user if existing_user else None

