from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, func
from app.db import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    age = Column(Integer, nullable=True)
    registered_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    password = Column(String(255), nullable=False)

    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")