from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 控制力
class ExaminationControl(Base):
    __tablename__ = 'examination_control'

    examination_control_id = Column(VARCHAR(20), primary_key=True, comment="控制力表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    examination_Control = Column(VARCHAR(20), nullable=False, comment="控制力")

    baseInfo = relationship("BaseInfo", back_populates='examinationControl')
