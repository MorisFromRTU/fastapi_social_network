from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import db, auth, security, schemas, database, crud
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
router = APIRouter()

@router.get('/')
async def get_posts(db: AsyncSession = Depends(db.get_db)):
    return await crud.get_posts(db=db)
    
@router.get('/{post_id}')
async def get_post(post_id: int, db: AsyncSession = Depends(db.get_db)):
    return await crud.get_post(post_id=post_id, db=db)


@router.post('/')
async def create_post(  
    post_data: schemas.PostCreate, 
    current_user: schemas.User = Depends(auth.get_current_user), 
    db: AsyncSession = Depends(db.get_db)
):
    post_data.author_id = current_user.id
    return await crud.create_post(post_data=post_data, db=db)

@router.delete('/{post_id}')
async def delete_post(
    post_id: int, 
    current_user: schemas.User = Depends(auth.get_current_user),
    db: AsyncSession = Depends(db.get_db)
):
    author_id = current_user.id
    return await crud.delete_post(post_id=post_id, db=db, author_id=author_id)

@router.patch('/{post_id}')
async def update_post(
    post_id: int,
    post_data: schemas.Post, 
    current_user: schemas.User = Depends(auth.get_current_user),
    db: AsyncSession = Depends(db.get_db)
):
    author_id = current_user.id
    return await crud.update_post(post_id=post_id, post_data=post_data, db=db, author_id=author_id)