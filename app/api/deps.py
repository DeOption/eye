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
from app.crud import crud_user
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
    db: Session = Depends(get_db), token: str = Depends(oauth2)
) -> User:
    # print(token1)
    # token: dict = {}
    # token["access_token"] = token1["access_token"]
    # token["token_type"] = token1["token_type"]
    try:
        payload = jwt.decode(
            token, setting.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = TokenPayLoad(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="token验证失败",
        )
    user = crud_user.user.getUser(db=db, uid=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="没有此用户")
    return user
