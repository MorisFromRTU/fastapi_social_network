from sqlalchemy import Column, Integer, String
from app.db import Base

class HelloItem(Base):
    __tablename__ = "hellos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
    def __repr__(self) -> str:
        return f"HelloItem = {self.title!r})"