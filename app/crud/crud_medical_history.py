from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.medical_history import MedicalHistory
from app.snow.snowflake import worker
from typing import Any

class CRUDMedicalHistory(CRUDBase[None, MedicalHistory, None]):
    def createMedicalHistory(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加病史
        :param db: 数据库连接对象
        :param medical_history_id: 病例ID
        :param data: {surgery_history, glasses_history, amblyopia_history, home_history, born_history, surgery_history_edit, now_age, now_wt, now_fs}
        :return: None
        """
        medical_history_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = MedicalHistory(
            base_info_id=base_info_id,
            medical_history_id=medical_history_id,
            **data
        )

        return db_obj

    def updateMedicalHistory(self, db: Session, id: str, data: dict) -> Any:
        """修改病例详情"""
        data = jsonable_encoder(data)
        db.query(MedicalHistory).filter(MedicalHistory.base_info_id == id).update(data)

        return None

medicalhistory = CRUDMedicalHistory(MedicalHistory)