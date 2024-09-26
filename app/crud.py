from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import database, logger, schemas
from fastapi import HTTPException, status, Depends


async def get_items(db: AsyncSession, model):
    query = select(model)
    result = await db.execute(query)  
    items = result.scalars().all()  
    return items

async def get_users(db: AsyncSession) -> list:
    users = await get_items(db=db, model=database.User)
    return users

async def get_user_by_username(db: AsyncSession, username: str) -> database.models.User:
    query = select(database.models.User).filter(database.models.User.username == username)
    result = await db.execute(query)
    existing_user = result.scalars().first()
    return existing_user if existing_user else None

async def get_user_by_id(db: AsyncSession, user_id: int) -> database.models.User:
    query = select(database.models.User).filter(database.models.User.id == user_id)
    result = await db.execute(query)
    existing_user = result.scalars().first()
    return existing_user if existing_user else None

async def delete_user(db: AsyncSession, user_id: int):
    user = await get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    await db.delete(user)
    await db.commit()
    return {"message": "User has been deleted successfully"}


async def get_posts(db: AsyncSession):
    posts = await get_items(db=db, model=database.Post)
    return posts

async def create_post(db: AsyncSession, post_data: schemas.PostCreate):
    post = database.Post(
        title=post_data.title,
        content=post_data.content,
        author_id=post_data.author_id
    )
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post