from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.schemas.user import User, UserCreate, UserUpdate
from typing import Optional, Dict, Union, Any
from app.core.security import verify_password, get_password_hash

from app.models import user


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    '''
        通过id获取用户
    '''
    def get_by_uid(
            self,
            db: Session,
            uid: str
    ) -> Optional[User]:
        return db.query(User).filter(User.uid == uid).first()

    '''
        注册时使用
    '''
    def create(
            self,
            db: Session,
            obj_in: UserCreate
    ) -> User:
        db_obj = User(
            name=obj_in.name,
            password=obj_in.password,
            email=obj_in.email,
            phone=obj_in.phone,
            permission=obj_in.permission
        )
        db.add(db_obj)
        db.commit()
        return db_obj

    '''
        更新
    '''
    def update(
            self,
            db: Session,
            db_obj: User,
            obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    '''
        验证用户登录
    '''
    @classmethod
    def authenticate(
            self,
            db: Session,
            name: str,
            password: str,
    ) -> Optional[User]:
        users = db.query(user.User).filter(
            user.User.name == name
        ).first()
        if not users:
            return None
        if not verify_password(password,  hashed_password):
            return None
        return users
