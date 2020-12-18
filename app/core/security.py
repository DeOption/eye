from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt
from app.core.config import setting
from app.utils.md5 import md5

ALGORITHM = "HS256"


def create_access_token(
        subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    """
    # 生成token
    :param subject: 保存到token的值
    :param expires_delta: 过期时间
    :return:
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def password_hash(login_password: str) -> str:
    """
    获取 hash 后的密码
    :param password:
    :return:
    """
    # login_password = bytes(login_password)
    setting.SECRET_KEY = md5(login_password)
    return md5(login_password)


def vertify_password(login_password, db_password) -> bool:
    """
    验证密码
    :param plain_password: 原密码
    :param hashed_password: hash后的密码
    :return:
    """
    md5_password = md5(login_password)
    return md5_password == db_password
