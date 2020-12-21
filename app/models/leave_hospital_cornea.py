from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 角膜映光(出院)
class LeaveHospitalCornea(Base):
    __tablename__ = 'leave_hospital_cornea'

    leave_hospital_cornea_id = Column(VARCHAR(20), primary_key=True, comment="角膜映光(出院)表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    examination_cornea_sp = Column(VARCHAR(20), nullable=False, comment="水平值")
    examination_cornea_cz = Column(VARCHAR(20), nullable=False, comment="垂直值（R/L or L/R）")
    examination_cornea_cz_z = Column(VARCHAR(20), nullable=False, comment="0-45, >45 垂直数值")

    baseInfo = relationship("BaseInfo", back_populates='leaveHospitalCornea')
