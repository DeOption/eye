from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 三棱镜(出院)
class LeaveHospitalSlj(Base):
    __tablename__ = 'leave_hospital_slj_id'

    leave_hospital_slj_id = Column(VARCHAR(20), primary_key=True, comment="三棱镜(出院)表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    leave_hospital_slj_near = Column(VARCHAR(10), comment="视近")
    leave_hospital_slj_far = Column(VARCHAR(20), comment="视远")

    baseInfo = relationship("BaseInfo", back_populates='leaveHospitalSlj')
