from pydantic import BaseModel, ConfigDict, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


class Token(BaseModel):
    access_token: str
    token_type: str
<<<<<<< HEAD


class TokenData(BaseModel):
    username: str | None = None


class FilterPage(BaseModel):
    offset: int = 0
    limit: int = 100
=======
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
