from fastapi import APIRouter, Depends
from app.api.deps import get_current_user
from app.api.api_v1.endpoints import login, register, user, case

api_router = APIRouter()

api_router.include_router(login.router, tags=["医生用户"])
api_router.include_router(register.router, tags=["医生用户"])
api_router.include_router(user.router, tags=["医生用户"])
api_router.include_router(case.router, dependencies=[Depends(get_current_user)], tags=["病例"])
