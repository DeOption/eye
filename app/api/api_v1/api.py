from fastapi import APIRouter

from app.api.api_v1.endpoints import user, login, register

api_router = APIRouter()

api_router.include_router(login.router, tags=["登录"])
api_router.include_router(register.router, tags=["注册"])
#api_router.include_router(user.router, prefix="/user", tags=["user"])