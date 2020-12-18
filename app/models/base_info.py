from sqlalchemy import Column, VARCHAR, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

class BaseInfo(Base):
    __tablename__ = 'base_info'

    base_info_id = Column(VARCHAR(20), primary_key=True, comment="基本信息id")
    base_ref_id = Column(VARCHAR(20), ForeignKey('base_ref.base_ref_id'), comment="中间表id")
    uid = Column(VARCHAR(20), nullable=False, comment="患者id")
    data_type = Column(VARCHAR(20), nullable=False, comment="数据类别")
    name = Column(VARCHAR(20), nullable=False, comment="姓名")
    sex = Column(VARCHAR(2), nullable=False, comment="性别")
    age = Column(VARCHAR(10), nullable=False, comment="年龄")
    id_number = Column(VARCHAR(18), nullable=False, comment="身份证号")
    phone_number = Column(VARCHAR(11), nullable=False, comment="手机号")
    order_number = Column(VARCHAR(20), nullable=False, comment="登记号/顺序号")

    base_refs = relationship("BaseRef", back_populates="base_infos")