from .users import router as users_router
from .posts import router as posts_router
from .comments import router as comments_router
__all__ = ["users_router", "posts_router", "comments_router"]