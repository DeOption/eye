from sqlalchemy import Column, VARCHAR, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 手术设计
class Surgery(Base):
    __tablename__ = 'surgery'

    surgery_id = Column(VARCHAR(20), primary_key=True, comment="手术设计表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    surgery_yb = Column(VARCHAR(20), nullable=False, comment="手术设计眼别")
    muscle = Column(Boolean, nullable=False, comment="肌肉")
    way = Column(VARCHAR(20), nullable=False, comment="方式")
    value = Column(VARCHAR(20), nullable=False, comment="量值")
    beizhu = Column(VARCHAR(20), nullable=False, comment="备注")

    baseInfo = relationship("BaseInfo", back_populates='surgery1')
