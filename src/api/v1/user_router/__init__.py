from fastapi import APIRouter, Depends
from libs.db import get_async_db, AsyncSession
from models import UserModel
from services.user_service import UserService
from .get_user_by_id import get_user_by_id

user_router = APIRouter(prefix="/users")


@user_router.get("/{id}")
async def get_user_by_id_route(
    id: int,
    db: AsyncSession = Depends(get_async_db),
    user_service: UserService = Depends(UserService),
):
    return await get_user_by_id(
        db=db, id=id, user_service=user_service
    )


def create_user_router() -> APIRouter:
    return user_router
