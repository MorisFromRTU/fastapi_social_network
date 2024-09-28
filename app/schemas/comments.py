from pydantic import BaseModel
from typing import Optional

class CommentCreate(BaseModel):
    content: str
    author_id: Optional[int] = None
    