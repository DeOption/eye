from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 三棱镜
class ExaminationSlj(Base):
    __tablename__ = 'examination_slj'

    examination_slj_id = Column(VARCHAR(20), primary_key=True, comment="三棱镜表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    examination_slj_zj_near = Column(VARCHAR(10), nullable=False, comment="视近(直角)")
    examination_slj_zj_far = Column(VARCHAR(20), nullable=False, comment="视远(直角)")
    examination_slj_dy_near = Column(VARCHAR(20), nullable=False, comment="视近(等腰)")
    examination_slj_dy_far = Column(VARCHAR(20), nullable=False, comment="视远(等腰)")
    examination_slj_cz = Column(VARCHAR(20), nullable=False, comment="垂直三棱镜")
    examination_slj_cz_z = Column(VARCHAR(20), nullable=False, comment="0-50")
    k_method = Column(VARCHAR(20), nullable=False, comment="k法")

    baseInfo = relationship("BaseInfo", back_populates='examinationSlj')
