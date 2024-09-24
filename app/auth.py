from .schemas import UserRegister
from . import crud, security, database, db
from fastapi import HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .database import User
from .security import verify_password
from .logger import logging


async def authenticate_user(db: AsyncSession, username: str, password: str):
    user: User = crud.get_user(db=db, username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

async def register_user(user: UserRegister, db: AsyncSession = Depends(db.get_db)):
    existing_user = await crud.get_user(db=db, username=user.username)
    if existing_user is not None:
        print(existing_user)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )
    
    hashed_password = await security.get_password_hash(user.password)

    user = database.User(
        username=user.username,
        name=user.name,
        surname=user.surname,
        email=user.email,
        password=hashed_password
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return {"message": "User created successfully", "user_id": user.id}