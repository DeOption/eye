from sqlalchemy import Column, VARCHAR, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 同视机
class ExaminationTsj(Base):
    __tablename__ = 'examination_tsj'

    examination_tsj_id = Column(VARCHAR(20), primary_key=True, comment="同视机表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    examination_tsj_tss = Column(Boolean, nullable=False, comment="同时视")
    examination_tsj_tss_sp = Column(VARCHAR(20), nullable=False, comment="同时视水平值")
    examination_tsj_tss_cz = Column(VARCHAR(20), nullable=False, comment="	同时视垂直值（R/L or L/R")
    examination_tsj_tss_cs_z = Column(VARCHAR(20), nullable=False, comment="		同时视垂直值具体数值")

    baseInfo = relationship("BaseInfo", back_populates='examinationTsj')
