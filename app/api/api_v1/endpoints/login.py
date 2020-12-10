from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic.datetime_parse import timedelta
from sqlalchemy.orm import Session
from app.crud import crud_user

from app.core import security
from app.core.config import setting
from app.api import deps



router = APIRouter()


@router.post("/login/access-token", summary="用户登录认证")
def login_access_token(
        *,
        db: Session = Depends(deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends(),
) -> Any:
    """
        用户JWT登录
        :param db:
        :param user_info:
        :return:
    """
    # 验证用户
    user = crud_user.CRUDUser.authenticate(
        db=db,
        name=form_data.username,
        password=form_data.password,
    )
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    # 查看token有无过期
    access_token_expires = timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }



'''
@router.post("/login/test-token", summary="测试登录认证")
def test_token(current_user: models.user = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user
'''