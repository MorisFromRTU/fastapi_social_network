from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import db, auth, crud, security, schemas, database
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any

router = APIRouter()

@router.get('/')
async def get_posts(db: AsyncSession = Depends(db.get_db)):
    return await crud.get_posts(db=db)
    
@router.post('/create')
async def create(
    post_data: schemas.PostCreate, 
    current_user: schemas.User = Depends(auth.get_current_user), 
    db: AsyncSession = Depends(db.get_db)
):
    post_data.author_id = current_user.id
    return await crud.create_post(post_data=post_data, db=db)
