from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .. import database, crud, schemas
from fastapi import HTTPException, status
from sqlalchemy.orm import selectinload

async def get_posts(db: AsyncSession):
    posts = await crud.get_items(db=db, model=database.Post)
    return posts

async def get_post(post_id: int, db: AsyncSession) -> database.Post:
    result = await db.execute(
        select(database.Post)
        .options(selectinload(database.Post.comments))
        .where(database.Post.id == post_id)
    )
    return result.scalars().first()

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

async def delete_post(db: AsyncSession, post_id: int, author_id: int):
    post: schemas.Post = await get_post(db=db, post_id=post_id)
    if post.author_id != author_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to delete this post."
        )
    await db.delete(post)
    await db.commit()
    return {"message": "Post has been deleted successfully"}

async def update_post(post_id: int, db: AsyncSession, post_data: schemas.PostUpdate, author_id: int):
    post = await get_post(db=db, post_id=post_id)
    if post.author_id != author_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to change this comment."
        )
    
    for var, value in vars(post_data).items():
        setattr(post, var, value) if value else None

    db.add(post)
    db.commit()
    db.refresh(post)
    return post

