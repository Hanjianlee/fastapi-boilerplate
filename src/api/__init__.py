from fastapi import APIRouter
from .v1 import create_v1_routers

APP_BASE_URL = "/api"

api_router = APIRouter(prefix=APP_BASE_URL)
api_router.include_router(create_v1_routers())


def create_app_router() -> APIRouter:
    return api_router
