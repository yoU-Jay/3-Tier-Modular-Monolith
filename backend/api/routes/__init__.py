from fastapi import APIRouter
from backend.api.routes import health_routes, user_routes
from .test_db import router as test_db_router



router = APIRouter()
router.include_router(health_routes.router, tags=["Health"])
router.include_router(user_routes.router, tags=["Users"])

router.include_router(test_db_router, prefix="/test", tags=["DB Test"])