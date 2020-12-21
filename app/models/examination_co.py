from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 电脑验光
class ExaminationCo(Base):
    __tablename__ = 'examination_co'

    examination_co_id = Column(VARCHAR(20), primary_key=True, comment="电脑验光表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    eye_type = Column(VARCHAR(10), nullable=False, comment="眼别")
    ds = Column(VARCHAR(20), nullable=False, comment="DS")
    dc = Column(VARCHAR(20), nullable=False, comment="DC")
    a = Column(VARCHAR(20), nullable=False, comment="A")

    baseInfo = relationship("BaseInfo", back_populates='examinationCo')
