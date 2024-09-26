from app.routers import hello_router, users_router, posts_router
from fastapi import FastAPI

def setup_routes(app: FastAPI):
    app.include_router(hello_router, prefix="/hello")
    app.include_router(users_router, prefix="/users")
    app.include_router(posts_router, prefix="/posts")