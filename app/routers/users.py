from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import UserRegister
from fastapi.security import OAuth2PasswordRequestForm
from ..db import get_db
from .. import auth
from .. import crud
from .. import security


router = APIRouter()

@router.get('/')
async def users(db: AsyncSession = Depends(get_db)):
    return await crud.get_users(db=db)

@router.get('/')
async def user(username: str, db: AsyncSession = Depends(get_db)):
    return await crud.get_user(db=db, username=username)

@router.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await security.login_for_access_token(form_data)

@router.post('/register')
async def register(user: UserRegister, db: AsyncSession = Depends(get_db)):
    return await auth.register_user(db=db, user=user)