from pydantic import BaseModel


class HelloItem(BaseModel):
    id: int
    title: str
