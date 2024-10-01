from pydantic import BaseModel
from typing import Optional

class CommentCreate(BaseModel):
    post_id: int
    content: str
    author_id: Optional[int] = None
    
