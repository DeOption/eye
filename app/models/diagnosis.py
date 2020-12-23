from sqlalchemy import Column, VARCHAR, ForeignKey, BOOLEAN
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 诊断
class Diagnosis(Base):
    __tablename__ = 'diagnosis'

    diagnosis_id = Column(VARCHAR(20), primary_key=True, comment="诊断表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    # diagnosis_strabismus_type = Column(VARCHAR(20), nullable=False, comment="斜视类型")
    latent_strabismus = Column(BOOLEAN, nullable=False, comment="隐斜视")
    Internal_strabismus = Column(VARCHAR(20), nullable=False, comment="内斜视")
    Exotropia = Column(VARCHAR(20), nullable=False, comment="外斜视")
    A_V = Column(VARCHAR(20), nullable=False, comment="A⁃V斜视")
    V = Column(VARCHAR(20), nullable=False, comment="垂直旋转性斜视")
    S = Column(VARCHAR(20), nullable=False, comment="特殊类型斜视")
    PS = Column(VARCHAR(20), nullable=False, comment="中枢性麻痹性斜视")
    N = Column(BOOLEAN, nullable=False, comment="眼球震颤")
    other = Column(BOOLEAN, nullable=False, comment="其他")

    baseInfo = relationship("BaseInfo", back_populates='diagnosis1')
    diagnosisStrabismusTypeInternal = relationship("DiagnosisStrabismusTypeInternal", back_populates='diagnosis_In',
                                           cascade='all, delete, delete-orphan')
