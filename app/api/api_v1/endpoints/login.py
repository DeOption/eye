from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic.datetime_parse import timedelta
from sqlalchemy.orm import Session
from app.crud import crud_user
from app.core import security
from app.core.config import setting
from app.api import deps

router = APIRouter()


@router.post('/user_login', summary="用户登录")
def login(
        *,
        db: Session = Depends(deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)
) -> dict:
    """
        用户JWT登录
        :param db:
        :param user_info:
        :return:
    """
    user = crud_user.CRUDUser.authenticate(
        db=db,
        user_name=form_data.username,
        password=form_data.password
    )
    if not user:
        return {
                "return_code": -1,
                "return_msg": "认证失败"
        }

    access_token_expires = timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "return_code": 0,
        "return_msg": "OK",
        "uid": user.uid,
        "access_token": security.create_access_token(
            user.uid, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
