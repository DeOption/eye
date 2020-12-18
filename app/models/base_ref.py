from sqlalchemy import Column, VARCHAR, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base


class BaseRef(Base):
    __tablename__ = 'base_ref'

    base_ref_id = Column(VARCHAR(20), primary_key=True, comment="中间表id")
    uid = Column(VARCHAR(20), ForeignKey('user.uid'), comment="用户id")
    create_time = Column(DateTime, comment="创建时间")
    modify_time = Column(DateTime, comment="修改时间")
    suifang = Column(DateTime, comment="随访时间")
    beizhu = Column(Text, comment="备注")

    users = relationship("User", back_populates='base_refs')
    base_infos = relationship("BaseInfo", back_populates="base_refs", cascade="all, delete, delete-orphan")
