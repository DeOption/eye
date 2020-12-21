from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 立体视（出院）
class LeaveHospitalLts(Base):
    __tablename__ = 'leave_hospital_lts'

    LeaveHospitalLtsid = Column(VARCHAR(20), primary_key=True, comment="立体视(出院)表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    examination_lts_j = Column(VARCHAR(20), nullable=False, comment="近方随机点立体视")
    examination_lts_y = Column(VARCHAR(20), nullable=False, comment="远方随机点立体视")

    baseInfo = relationship("BaseInfo", back_populates='leaveHospitalLts')
