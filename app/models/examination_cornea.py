from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 角膜映光
class ExaminationCornea(Base):
    __tablename__ = 'examination_cornea'

    examination_cornea_id = Column(VARCHAR(20), primary_key=True, comment="角膜映光表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    eye_type = Column(VARCHAR(10), comment="眼别")
    examination_cornea_sp = Column(VARCHAR(20), comment="水平值")
    examination_cornea_cz = Column(VARCHAR(20), comment="垂直值（R/L or L/R）")
    examination_cornea_cz_z = Column(VARCHAR(20), comment="0-45, >45 垂直数值")

    baseInfo = relationship("BaseInfo", back_populates='examinationCornea')
