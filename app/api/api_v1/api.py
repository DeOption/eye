from fastapi import APIRouter

from app.api.api_v1.endpoints import login, register, user, case

api_router = APIRouter()

api_router.include_router(login.router, tags=["登录"])
api_router.include_router(register.router, tags=["注册"])
api_router.include_router(user.router, tags=["获取用户信息"])
api_router.include_router(case.router, tags=["获取病例列表"])
