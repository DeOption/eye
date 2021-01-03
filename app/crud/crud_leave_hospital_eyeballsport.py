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
        leave_hospital_eyeballsport_id_left = worker.get_id()
        leave_hospital_eyeballsport_id_right = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = [
            LeaveHospitalEyeballsport(
                base_info_id=base_info_id,
                leave_hospital_eyeballsport_id=leave_hospital_eyeballsport_id_left,
                eye_type="left",
                **data["left"]
            ),
            LeaveHospitalEyeballsport(
                base_info_id=base_info_id,
                leave_hospital_eyeballsport_id=leave_hospital_eyeballsport_id_right,
                eye_type="right",
                **data["right"]
            )
        ]
        db.add_all(db_obj)
        db.commit()
        db.close()
        return db_obj

    def updateLeaveHospitalEyeballsport(self, db: Session, id: str, data: dict) -> Any:
        """修改眼球运动（出院）"""
        data = jsonable_encoder(data)
        db.query(LeaveHospitalEyeballsport).\
            filter(LeaveHospitalEyeballsport.base_info_id == id, LeaveHospitalEyeballsport.eye_type == "left").\
            update(data["left"])
        db.query(LeaveHospitalEyeballsport).\
            filter(LeaveHospitalEyeballsport.base_info_id == id, LeaveHospitalEyeballsport.eye_type == "right").\
            update(data["right"])
        db.commit()
        db.close()
        return None

leavehospitaleyeballsport = CRUDLeaveHospitalEyeballsport(LeaveHospitalEyeballsport)