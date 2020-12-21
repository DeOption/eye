from sqlalchemy import Column, VARCHAR, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 内斜视类型
class DiagnosisStrabismusTypeInternal(Base):
    __tablename__ = 'diagnosis_strabismus_type_internal'

    diagnosis_strabismus_type_internal_id = Column(VARCHAR(20), primary_key=True, comment="内斜视表id")
    diagnosis_id = Column(VARCHAR(20), ForeignKey('diagnosis.diagnosis_id'), comment="诊断表id")
    IE = Column(VARCHAR(20), nullable=False, comment="先天性(婴儿型)内斜视")
    CE = Column(Boolean, nullable=False, comment="共同性内斜视")
    SE = Column(VARCHAR(20), nullable=False, comment="继发性内斜视")
    NE = Column(VARCHAR(20), nullable=False, comment="非共同性内斜视")
    EN = Column(VARCHAR(20), nullable=False, comment="伴有眼球震颤的内斜视")

    diagnosis_In = relationship("Diagnosis", back_populates='diagnosisStrabismusTypeInternal')
