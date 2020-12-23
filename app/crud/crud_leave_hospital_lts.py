from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.leave_hospital_lts import LeaveHospitalLts
from app.snow.snowflake import worker
from typing import Any

class CRUDLeaveHospitalLts(CRUDBase[None, LeaveHospitalLts, None]):
    def createLeaveHospitalLts(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加立体视（出院）
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {examination_lts_j, examination_lts_y}
        :return: None
        """
        LeaveHospitalLtsid = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = LeaveHospitalLts(
            base_info_id=base_info_id,
            LeaveHospitalLtsid=LeaveHospitalLtsid,
            **data
        )
        db.add(db_obj)
        db.commit()
        return db_obj

leavehospitallts = CRUDLeaveHospitalLts(LeaveHospitalLts)