from sqlalchemy import Column, VARCHAR, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 眼球运动
class ExaminationEyeballsport(Base):
    __tablename__ = 'examination_eyeballsport'

    examination_eyeballsport_id = Column(VARCHAR(20), primary_key=True, comment="眼球运动表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    eye_type = Column(VARCHAR(10), nullable=False, comment="眼别")
    normal = Column(Boolean, nullable=False, comment="正常")
    external_rectus = Column(VARCHAR(20), nullable=False, comment="	外直肌")
    internal_rectus = Column(VARCHAR(20), nullable=False, comment="	内直肌")
    pper_rectus = Column(VARCHAR(20), nullable=False, comment="上直肌")
    lower_rectus = Column(VARCHAR(20), nullable=False, comment="下直肌")
    upper_oblique = Column(VARCHAR(20), nullable=False, comment="上斜肌")
    lower_oblique = Column(VARCHAR(20), nullable=False, comment="下斜肌")

    baseInfo = relationship("BaseInfo", back_populates='examinationEyeballsport')
