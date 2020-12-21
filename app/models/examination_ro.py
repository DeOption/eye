from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 检影验光
class ExaminationRo(Base):
    __tablename__ = 'examination_ro'

    examination_ro_id = Column(VARCHAR(20), primary_key=True, comment="检影验光表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    eye_type = Column(VARCHAR(10), nullable=False, comment="眼别")
    ds = Column(VARCHAR(20), nullable=False, comment="DS")
    dc = Column(VARCHAR(20), nullable=False, comment="DC")
    a = Column(VARCHAR(20), nullable=False, comment="A")

    baseInfo = relationship("BaseInfo", back_populates='examinationRo')
