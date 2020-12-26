from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.schemas.user import UserCreate, UserUpdate
from app.models.users import User
from typing import Optional, Dict, Union, Any
from app.core.security import password_hash, vertify_password
from app.snow.snowflake import worker
from app.models import users
from app.core import security


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    '''
        通过id获取用户
    '''

    def get_by_uid(
            self,
            *,
            db: Session,
            name: str
    ) -> Optional[User]:
        return db.query(users.User).filter(users.User.name == name).first()


    '''
        通过id获取用户信息
    '''
    def getUser(
            self,
            db: Session,
            uid: str
    ) -> User:
        return db.query(users.User).filter(users.User.uid == uid).first()


    '''
        注册时使用
    '''

    def add(
            self,
            db: Session,
            name: str,
            password: str,
            email: str,
            phone: str
    ) -> User:
        uid = worker.get_id()
        password=security.password_hash(password)
        db_obj = User(
            uid=uid,
            name=name,
            password=password,
            email=email,
            phone=phone,
            permission=1
        )
        db.add(db_obj)
        db.commit()
        db.close()
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
            hashed_password = password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)
    '''
        验证用户登录
    '''

    @classmethod
    def authenticate(
            self,
            user_name: str,
            db: Session,
            password: str,
    ) -> Optional[User]:
        user = db.query(users.User).filter(
            users.User.name == user_name
        ).first()
        if not user:
            return None
        if not vertify_password(password, user.password):
            return None
        return user


user = CRUDUser(users.User)