from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.leave_hospital_slj import LeaveHospitalSlj
from app.snow.snowflake import worker
from typing import Any

class CRUDLeaveHospitalSlj(CRUDBase[None, LeaveHospitalSlj, None]):
    def createLeaveHospitalSlj(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加三棱镜（出院）
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {leave_hospital_slj_near, leave_hospital_slj_far}
        :return: None
        """
        leave_hospital_slj_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = LeaveHospitalSlj(
            base_info_id=base_info_id,
            leave_hospital_slj_id=leave_hospital_slj_id,
            **data
        )
        db.add(db_obj)
        db.commit()
        return db_obj

leavehospitalslj = CRUDLeaveHospitalSlj(LeaveHospitalSlj)