from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: Optional[str] = None
    phone: int = None


class UserAuth(BaseModel):
    password: str


# 创建账号需要验证的条件
class UserCreate(UserBase):
    name: str
    email: str
    password: str
    permission: int

# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UserInDB(UserInDBBase):
    hashed_password: str


class User(UserInDBBase):
    pass
