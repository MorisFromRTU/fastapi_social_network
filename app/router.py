from app.routers import users_router, posts_router, comments_router
from fastapi import FastAPI

def setup_routes(app: FastAPI):
    app.include_router(users_router, prefix="/users")
    app.include_router(posts_router, prefix="/posts")
    app.include_router(comments_router, prefix="/comments")