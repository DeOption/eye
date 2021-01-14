from fastapi import APIRouter, Depends, HTTPException, Body, status
from sqlalchemy.orm import Session
from app.api import deps
from app.crud.crud_user import user
from typing import Optional
import re

router = APIRouter()


@router.post('/user_register', summary="用户注册")
def register(
        db: Session = Depends(deps.get_db),
        name: Optional[str] = Body(..., description='用户名'),
        password: Optional[str] = Body(..., description='密码'),
        email: Optional[str] = Body(..., description='邮箱'),
        phone: Optional[str] = Body(..., description='手机号')
) -> dict:
    """
    用户注册
    :param db: 数据库
    :return: 返回
    """
    partten = "[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
    format_email = re.findall(pattern=partten, string=email)
    if (len(password) != 8) or (len(phone) != 11) or format_email is None:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="注册失败，密码长度必须为8位，并填写正确手机号码"
        )
    try:
        user.add(db=db, name=name, password=password, email=email, phone=phone)
        pass
    except Exception as e:
        print(e)
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "return_code": -1,
                "return_msg": "注册失败，请填写正确信息: " + str(e)
            },
        )
    return {
        "return_code": 0,
        "return_msg": "OK"
    }
