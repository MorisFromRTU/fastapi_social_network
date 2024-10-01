from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import CommentCreate
from .. import database, crud
from fastapi import HTTPException, status

async def get_comment(db: AsyncSession, comment_id: int) -> database.Comment:
    comment = await crud.get_item(item_id=comment_id, model=database.Comment, db=db)
    return comment

async def add_comment(db: AsyncSession, comment_data: CommentCreate):
    comment = database.Comment(
        content=comment_data.content,
        author_id=comment_data.author_id,
        post_id=comment_data.post_id
    )
    db.add(comment)
    await db.commit()
    await db.refresh(comment)
    return comment

async def delete_comment(comment_id: int, db: AsyncSession, author_id: int):
    comment = await get_comment(comment_id=comment_id, db=db)
    if author_id != comment.author_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to delete this comment."
        )
    await db.delete(comment)
    await db.commit()
    return {"message": "Comment has been deleted successfully"}