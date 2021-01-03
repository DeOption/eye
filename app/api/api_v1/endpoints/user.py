from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from typing import Optional
from app.crud import crud_user
from app.api.deps import get_current_user
from app.models.users import User

router = APIRouter()


@router.get('/get_user_info', summary="获取用户信息")
def userInfo(
        db: Session = Depends(deps.get_db),
        uid: Optional[str] = Query(None, description='用户id'),
        current_user: Optional[User] = Depends(get_current_user)
) -> dict:
    """
    :param db:
    :param uid:
    :return:
    """

    user = crud_user.user.getUser(db=db, uid=uid)
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="没有此用户！"
        )
    user_info = {
        'name': user.name,
        'email': user.email,
        'phone': user.phone
    }
    return {
        "return_code": 0,
        "return_msg": "OK",
        "user_info": user_info
    }

