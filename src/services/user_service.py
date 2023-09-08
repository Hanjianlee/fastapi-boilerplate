from libs.db import AsyncSession
from schemas import UserSchema
from crud import users


class UserService:
    def __init__(self) -> None:
        """handles user related operations"""

    async def get_user_by_id(
        self, db: AsyncSession, id: int
    ) -> UserSchema:
        result = await users.get_user_by_id(db=db, id=id)
        if result is not None:
            user = UserSchema(
                id=result.id,
                username=result.username,
                email=result.email,
            )
        return user


__all__ = ["UserService"]
