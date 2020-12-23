from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.leave_hospital_eyeballsport import LeaveHospitalEyeballsport
from app.snow.snowflake import worker
from typing import Any

class CRUDLeaveHospitalEyeballsport(CRUDBase[None, LeaveHospitalEyeballsport, None]):
    def createLeaveHospitalEyeballsport(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加眼球运动（出院）
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {eye_type, normal, external_rectus, internal_rectus, pper_rectus, lower_rectus, upper_oblique, lower_oblique}\n
        :return: None
        """
        leave_hospital_eyeballsport_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = LeaveHospitalEyeballsport(
            base_info_id=base_info_id,
            leave_hospital_eyeballsport_id=leave_hospital_eyeballsport_id,
            **data
        )
        db.add(db_obj)
        db.commit()
        return db_obj

leavehospitaleyeballsport = CRUDLeaveHospitalEyeballsport(LeaveHospitalEyeballsport)