
from sqlalchemy import Column, Integer, VARCHAR

from app.sqlDB.base_class import Base


class User(Base):
    __tablename__ = 'user'
    uid = Column(VARCHAR(20), primary_key=True, comment="用户id")
    name = Column(VARCHAR(20), nullable=False, comment="用户名")
    password = Column(VARCHAR(255), comment="密码")
    email = Column(VARCHAR(255), nullable=False, comment="邮箱")
    phone = Column(VARCHAR(11), comment="手机号")
    permission = Column(Integer(), comment="权限")
