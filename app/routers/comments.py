from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .. import db, crud, schemas, auth
from ..schemas import CommentCreate

router = APIRouter()

@router.post('/add')
async def add_comment(
    comment_data: CommentCreate, 
    current_user: schemas.User = Depends(auth.get_current_user), 
    db: AsyncSession = Depends(db.get_db)):
    comment_data.author_id = current_user.id
    return await crud.add_comment(db=db, comment_data=comment_data)

@router.get('/')
async def get_comments(post_id: int, db: AsyncSession = Depends(db.get_db)):
    post = await crud.get_post(post_id=post_id, db=db)
    return post.comments

@router.get('/{comment_id}')
async def get_comment(comment_id: int, db: AsyncSession = Depends(db.get_db)):
    comment = await crud.get_comment(comment_id=comment_id, db=db)
    return comment
                      
@router.delete('/{comment_id}')
async def delete_comment(
    comment_id: int, 
    current_user: schemas.User = Depends(auth.get_current_user),
    db: AsyncSession = Depends(db.get_db)):
    return await crud.delete_comment(
        comment_id=comment_id, 
        author_id=current_user.id, 
        db=db)