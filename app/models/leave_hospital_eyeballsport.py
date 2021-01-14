from sqlalchemy import Column, VARCHAR, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 眼球运动（出院）
class LeaveHospitalEyeballsport(Base):
    __tablename__ = 'leave_hospital_eyeballsport'

    leave_hospital_eyeballsport_id = Column(VARCHAR(20), primary_key=True, comment="眼球运动(出院)表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    eye_type = Column(VARCHAR(10), comment="眼别")
    normal = Column(Boolean, comment="正常")
    external_rectus = Column(VARCHAR(20), comment="	外直肌")
    internal_rectus = Column(VARCHAR(20), comment="	内直肌")
    upper_rectus = Column(VARCHAR(20), comment="上直肌")
    lower_rectus = Column(VARCHAR(20), comment="下直肌")
    upper_oblique = Column(VARCHAR(20), comment="上斜肌")
    lower_oblique = Column(VARCHAR(20), comment="下斜肌")

    baseInfo = relationship("BaseInfo", back_populates='leaveHospitalEyeballsport')
