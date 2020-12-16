from fastapi import FastAPI, Depends, Body
from sqlalchemy.orm import Session
from app.api.deps import get_db
from typing import Optional
router = FastAPI()

@router.post('/register/')
def register(
        *,
        db: Session = Depends(get_db),
        username: Optional[str] = Body(..., description='用户名'),
        password: Optional[str] = Body(..., description='密码'),
        email: Optional[str] = Body(..., description='邮箱')
) -> dict:

    pass
    return {
        'username': username,
        'password': password,
        'email': email
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(router, host='127.0.0.1', port=8000)