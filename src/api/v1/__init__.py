from fastapi import APIRouter
from .user_router import create_user_router

v1_routers = APIRouter(prefix="/v1")
v1_routers.include_router(create_user_router())


def create_v1_routers() -> APIRouter:
    return v1_routers
