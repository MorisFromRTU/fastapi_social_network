from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    

class PostCreate(BaseModel):
    title: str
    content: str
    author_id: Optional[int] = None
