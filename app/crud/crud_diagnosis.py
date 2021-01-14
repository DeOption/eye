from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.diagnosis import Diagnosis
from app.snow.snowflake import worker
from typing import Any

class CRUDDiagnosis(CRUDBase[None, Diagnosis, None]):
    def createDiagnosis(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加诊断
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {latent_strabismus, Internal_strabismus, Exotropia, A_V, V, S, PS, N, other}
        :return: None
        """
        diagnosis_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = Diagnosis(
            base_info_id=base_info_id,
            diagnosis_id=diagnosis_id,
            **data
        )

        return db_obj

    def updateDiagnosis(self, db: Session, id: str, data: dict) -> Any:
        """修改诊断"""
        data = jsonable_encoder(data)
        db.query(Diagnosis).filter(Diagnosis.base_info_id == id).update(data)

        return None

diagnosis = CRUDDiagnosis(Diagnosis)