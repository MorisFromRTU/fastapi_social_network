from .hello import router as hello_router
from .users import router as users_router
from .posts import router as posts_router
__all__ = ["hello_router", "users_router", "posts_router"]