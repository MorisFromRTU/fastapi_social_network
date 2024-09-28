from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .. import db, crud
from ..schemas import CommentCreate

router = APIRouter()


@router.post('/add')
async def add_comment(post_id: int, comment_data: CommentCreate, db: AsyncSession = Depends(db.get_db)):
    return await crud.add_comment(db=db, comment=comment_data, post_id=post_id)
