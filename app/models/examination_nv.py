from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

class ExaminationNv(Base):
    __tablename__ = 'examination_nv'

    examination_nv_id = Column(VARCHAR(20), primary_key=True, comment="裸眼视力表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    left = Column(VARCHAR(10), nullable=False, comment="裸左眼视力")
    right = Column(VARCHAR(10), nullable=False, comment="裸右眼视力")

    baseInfo = relationship("BaseInfo", back_populates='examinationNv')
