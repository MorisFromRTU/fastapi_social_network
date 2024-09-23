from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_db
from .. import crud
router = APIRouter()

@router.get('/')
async def users(db: AsyncSession = Depends(get_db)):
    return await crud.get_users(db=db)