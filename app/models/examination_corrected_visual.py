from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 矫正视力
class ExaminationCorrectedVisual(Base):
    __tablename__ = 'examination_corrected_visual'

    examination_corrected_visual_id = Column(VARCHAR(20), primary_key=True, comment="矫正视力表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    left = Column(VARCHAR(10), nullable=False, comment="左眼矫正视力")
    right = Column(VARCHAR(10), nullable=False, comment="右眼矫正视力")

    baseinfo = relationship("BaseInfo", back_populates='examinationCorrectedVisual')
