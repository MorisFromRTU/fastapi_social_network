from sqlalchemy import Column, Integer, String, DateTime
from datetime import timezone, datetime
from app.db import Base

class HelloItem(Base):
    __tablename__ = "hellos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
    def __repr__(self) -> str:
        return f"HelloItem = {self.title!r})"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    age = Column(Integer, nullable=True)
    registered_at = Column(DateTime, default=datetime.now(timezone.utc))
