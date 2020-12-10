from typing import Any, List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.schemas import user
from app import schemas
from app.api import deps
from app.crud import crud_user
from app.schemas import user

router = APIRouter()

'''
@router.get("/user")
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve users.
    """
    users = crud_user.get_multi(db, skip=skip, limit=limit)
    return users
'''

'''
@router.post("/user", response_model=schemas.user)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.user.UserCreate,
) -> Any:
    """
    Create new user.
    """
    user = crud_user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud_user.create(db, obj_in=user_in)
    return user
'''

'''
@router.get("/user/{user_id}", response_model=schemas.user)
def read_user_by_id(
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    user = crud_user.get(db, id=user_id)
    if user:
        return user
'''

'''
@router.put("/user/{user_id}", response_model=schemas.user)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: schemas.user.UserUpdate,
) -> Any:

    user = crud_user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud_user.update(db, db_obj=user, obj_in=user_in)
    return user
'''