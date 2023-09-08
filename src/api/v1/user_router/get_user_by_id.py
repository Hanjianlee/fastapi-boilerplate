from libs.db import AsyncSession
from schemas import UserSchema
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette import status
from services.user_service import UserService


async def get_user_by_id(
    db: AsyncSession, id: int, user_service: UserService
) -> UserSchema:
    try:
        user = user_service.get_user_by_id(db=db, id=id)
        return JSONResponse(
            content=user, status_code=status.HTTP_200_OK
        )
    except Exception as ext:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ext),
        ) from ext
