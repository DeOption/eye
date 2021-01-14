from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.examination_lts import ExaminationLts
from app.snow.snowflake import worker
from typing import Any

class CRUDExaminationLts(CRUDBase[None, ExaminationLts, None]):
    def createExaminationLts(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加立体视
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {examination_lts_j, examination_lts_y}
        :return: None
        """
        examination_lts_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = ExaminationLts(
            base_info_id=base_info_id,
            examination_lts_id=examination_lts_id,
            **data
        )

        return db_obj

    def updateExaminationLts(self, db: Session, id: str, data: dict) -> Any:
        """修改立体视"""
        data = jsonable_encoder(data)
        db.query(ExaminationLts).filter(ExaminationLts.base_info_id == id).update(data)

        return None

examinationlts = CRUDExaminationLts(ExaminationLts)