from sqlalchemy import Column, VARCHAR, Boolean, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

class MedicalHistory(Base):
    __tablename__ = 'medical_history'

    medical_history_id = Column(VARCHAR(20), primary_key=True, comment="病史表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    surgery_history = Column(Boolean, nullable=False, comment="手术史")
    glasses_history = Column(VARCHAR(20), nullable=False, comment="戴镜史")
    amblyopia_history = Column(Boolean, nullable=False, comment="弱视治疗")
    home_history = Column(Boolean, nullable=False, comment="家族史")
    born_history = Column(Boolean, nullable=False, comment="生产史")
    surgery_history_edit = Column(Text, nullable=False, comment="手术史补充mow_age")
    mow_age = Column(Integer, nullable=False, comment="斜视年龄")
    now_wt = Column(Boolean, nullable=False, comment="歪头")
    now_fs = Column(Boolean, nullable=False, comment="复视")

    baseinfo = relationship("BaseInfo", back_populates='medicalHistory')
