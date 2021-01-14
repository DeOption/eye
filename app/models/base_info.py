from sqlalchemy import Column, VARCHAR, DateTime, Text
from sqlalchemy.orm import relationship
from app.sqlDB.base_class import Base
from app.models.medical_history import MedicalHistory
from app.models.examination_cornea import ExaminationCornea
from app.models.examination_nv import ExaminationNv
from app.models.examination_corrected_visual import ExaminationCorrectedVisual
from app.models.examination_co import ExaminationCo
from app.models.examination_ro import ExaminationRo
from app.models.examination_tsj import ExaminationTsj
from app.models.examination_control import ExaminationControl
from app.models.examination_cornea import ExaminationCornea
from app.models.examination_slj import ExaminationSlj
from app.models.examination_lts import ExaminationLts
from app.models.leave_hospital_eyeballsport import LeaveHospitalEyeballsport
from app.models.diagnosis import Diagnosis
from app.models.surgery import Surgery
from app.models.leave_hospital_cornea import LeaveHospitalCornea
from app.models.leave_hospital_lts import LeaveHospitalLts
from app.models.leave_hospital_slj import LeaveHospitalSlj
from app.models.examination_eyeballsport import ExaminationEyeballsport
from app.models.diagnosis_strabismus_type_internal import DiagnosisStrabismusTypeInternal

class BaseInfo(Base):
    __tablename__ = 'base_info'

    id = Column(VARCHAR(20), primary_key=True, comment="基本信息id")
    data_type = Column(VARCHAR(20), nullable=False, comment="数据类别")
    user_name = Column(VARCHAR(20), nullable=False, comment="姓名")
    sex = Column(VARCHAR(8), nullable=False, comment="性别")
    age = Column(VARCHAR(20), nullable=False, comment="年龄")
    id_number = Column(VARCHAR(18), nullable=False, comment="身份证号")
    phone_number = Column(VARCHAR(11), nullable=False, comment="手机号")
    order_number = Column(VARCHAR(20), nullable=False, comment="登记号/顺序号")

    create_time = Column(DateTime, nullable=False, comment="创建时间")
    modify_time = Column(DateTime, nullable=False, comment="修改时间")
    suifang = Column(DateTime, nullable=False, comment="随访时间")
    beizhu = Column(Text, nullable=False, comment="备注")

    medicalHistory = relationship("MedicalHistory", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    examinationNv = relationship("ExaminationNv", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    examinationCorrectedVisual = relationship("ExaminationCorrectedVisual", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    examinationCo = relationship("ExaminationCo", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    examinationRo = relationship("ExaminationRo", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    examinationTsj = relationship("ExaminationTsj", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    examinationLts = relationship("ExaminationLts", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    examinationControl = relationship("ExaminationControl", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    examinationCornea = relationship("ExaminationCornea", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    examinationSlj = relationship("ExaminationSlj", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    examinationEyeballsport = relationship("ExaminationEyeballsport", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    #
    diagnosis1 = relationship("Diagnosis", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    surgery1 = relationship("Surgery", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    leaveHospitalLts = relationship("LeaveHospitalLts", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    leaveHospitalCornea = relationship("LeaveHospitalCornea", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    leaveHospitalSlj = relationship("LeaveHospitalSlj", back_populates='baseInfo', cascade='all, delete, delete-orphan')
    leaveHospitalEyeballsport = relationship("LeaveHospitalEyeballsport", back_populates='baseInfo', cascade='all, delete, delete-orphan')
