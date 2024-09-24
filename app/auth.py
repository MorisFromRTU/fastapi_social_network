from . import crud, security, database, db, schemas
from fastapi import HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta


async def authenticate_user(db: AsyncSession, username: str, password: str) -> database.User:
    user = await crud.get_user(db=db, username=username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    if not security.verify_password(password, user.password):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password"
        )
    return user


async def login_for_access_token(form_data: schemas.UserLogin, db: AsyncSession):
    user = await authenticate_user(username=form_data.username, password=form_data.password, db=db)
    access_token_expire = timedelta(minutes=30)
    access_token = await security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expire)
    return {"access_token": access_token, "token_type": "bearer"}


async def register_user(user: schemas.UserRegister, db: AsyncSession = Depends(db.get_db)):
    existing_user = await crud.get_user(db=db, username=user.username)
    if existing_user is not None:
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