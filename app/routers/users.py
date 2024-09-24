from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import db, auth, crud, security, schemas
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()

@router.get('/')
async def users(db: AsyncSession = Depends(db.get_db)):
    return await crud.get_users(db=db)

@router.get('/')
async def user(username: str, db: AsyncSession = Depends(db.get_db)):
    return await crud.get_user_by_username(db=db, username=username)

@router.get('/')
async def user(user_id: int, db: AsyncSession = Depends(db.get_db)):
    return await crud.get_user_by_id(db=db, user_id=user_id)

@router.delete('/')
async def delete_user(user_id: int, db: AsyncSession = Depends(db.get_db)):
    return await crud.delete_user(db=db, user_id=user_id)

@router.post('/login')
async def login(form_data: schemas.UserLogin, db: AsyncSession = Depends(db.get_db)):
    return await auth.login_for_access_token(form_data=form_data, db=db)

@router.post('/register')
async def register(user: schemas.UserRegister, db: AsyncSession = Depends(db.get_db)):
    return await auth.register_user(db=db, user=user)

