from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import UserModel


async def get_user_by_id(
    db_session: AsyncSession, id: int
) -> UserModel:
    result = await db_session.execute(
        select(UserModel).where(UserModel.id == id)
    )
    user = result.scalar_one_or_none()
    return user
