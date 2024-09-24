from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .database.models import User
from .schemas import UserRegister, UserItem
from .utils import get_or_404
from .security import verify_password, get_password_hash


async def get_users(db: AsyncSession) -> list:
    query = select(User)
    result = await db.execute(query)  
    users = result.scalars().all()  
    return users

async def get_user(db: AsyncSession, username: str) -> User:
    query = select(User).filter(User.username == username)
    result = await db.execute(query)
    existing_user = result.scalars().first()
    return existing_user if existing_user else None
    
async def register_user(db: AsyncSession, user: UserRegister) -> UserItem:
    
    return UserItem()
