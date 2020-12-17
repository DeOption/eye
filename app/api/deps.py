from typing import Generator, Optional, Any, Union
from pydantic import ValidationError
from app.sqlDB.session import SessionLocal
from app.models.users import User
from fastapi import Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core import security
from app.core.config import setting
from jose import jwt
from app.crud.crud_user import CRUDUser
from app.utils import custom_exc
from app.schemas.token import TokenPayLoad


oauth2 = OAuth2PasswordBearer(
    tokenUrl="/user_login".format(setting.API_V1_STR)
)

# 依赖
def get_db() -> Generator:
    """
        获取sqlalchemy会话对象
        :return: Generator
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
        *,
        db: Session = Depends(get_db),
        token: str = Depends(oauth2)
) -> User:
    """
       根据header中token 获取当前用户
       :param db:
       :param token:
       :return:
    """
    try:
        payload = jwt.encode(
            token, setting.SECRET_KEY, algorithm=[security.ALGORITHM]
        )
        token_data = TokenPayLoad(**payload)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码有误"
        )
    user = CRUDUser.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user