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


# def check_jwt_token(
#      token: Optional[str] = Header(...)
# ) -> Union[str, Any]:
#     """
#         解析验证token  默认验证headers里面为token字段的数据
#         可以给 headers 里面token替换别名, 以下示例为 X-Token
#         token: Optional[str] = Header(None, alias="X-Token")
#         :param token:
#         :return:
#     """
#
#     try:
#         payload = jwt.decode(
#             token,
#             setting.SECRET_KEY, algorithms=[setting.ALGORITHM]
#         )
#         return payload
#     except jwt.ExpiredSignatureError:
#         raise custom_exc.TokenExpired()
#     except (jwt.JWTError, ValidationError, AttributeError):
#         raise custom_exc.TokenAuthError()



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