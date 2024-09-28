from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import CommentCreate

async def add_comment(db: AsyncSession, comment: CommentCreate, post_id: int):
    return 1