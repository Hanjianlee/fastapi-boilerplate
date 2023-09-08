from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
