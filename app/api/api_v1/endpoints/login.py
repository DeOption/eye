from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic.datetime_parse import timedelta
from sqlalchemy.orm import Session
from app.crud import crud_user
from app.core import security
from app.core.config import setting
from app.api import deps
from app.schemas.token import Token



router = APIRouter()


@router.post('/user_login', response_model=Token, summary="用户登录认证")
def login(
        *,
        db: Session = Depends(deps.get_db),
        from_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)
) -> dict:
    """
        用户JWT登录
        :param db:
        :param user_info:
        :return:
    """
    user = crud_user.CRUDUser.authenticate(
        db=db,
        user_name=from_data.username,
        password=from_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码有误"
        )
    access_token_expires = timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.uid, expires_delta=access_token_expires
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