from typing import Generator, Optional, Any, Union

from pydantic import ValidationError

from app.sqlDB.session import SessionLocal
from app.models.user import User
from fastapi import Depends, Header
from sqlalchemy.orm import Session
from app.core.config import setting
from jose import jwt
from app.crud.crud_user import CRUDUser
from app.utils import custom_exc


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


def check_jwt_token(
     token: Optional[str] = Header(...)
) -> Union[str, Any]:
    """
        解析验证token  默认验证headers里面为token字段的数据
        可以给 headers 里面token替换别名, 以下示例为 X-Token
        token: Optional[str] = Header(None, alias="X-Token")
        :param token:
        :return:
    """

    try:
        payload = jwt.decode(
            token,
            setting.SECRET_KEY, algorithms=[setting.ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise custom_exc.TokenExpired()
    except (jwt.JWTError, ValidationError, AttributeError):
        raise custom_exc.TokenAuthError()


def get_current_user(
        *,
        db: Session = Depends(get_db),
        token: str = Depends(check_jwt_token)
) -> User:
    """
       根据header中token 获取当前用户
       :param db:
       :param token:
       :return:
    """
    user = CRUDUser.get(db, id=token.get("sub"))
    if not user:
        raise custom_exc.TokenAuthError(err_desc="User not found")
    return user

