from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.leave_hospital_cornea import LeaveHospitalCornea
from app.snow.snowflake import worker
from typing import Any

class CRUDLeaveHospitalCornea(CRUDBase[None, LeaveHospitalCornea, None]):
    def createLeaveHospitalCornea(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加角膜映光（出院）
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {examination_cornea_sp, examination_cornea_cz, examination_cornea_cz_z}\n
        :return: None
        """
        leave_hospital_cornea_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = LeaveHospitalCornea(
            base_info_id=base_info_id,
            leave_hospital_cornea_id=leave_hospital_cornea_id,
            **data
        )
        db.add(db_obj)
        db.commit()
        db.close()
        return db_obj

    def updateLeaveHospitalCornea(self, db: Session, id: str, data: dict) -> Any:
        """修改角膜映光（出院）"""
        data = jsonable_encoder(data)
        db.query(LeaveHospitalCornea).filter(LeaveHospitalCornea.base_info_id == id).update(data)
        db.commit()
        db.close()
        return None

leavehospitalcornea = CRUDLeaveHospitalCornea(LeaveHospitalCornea)