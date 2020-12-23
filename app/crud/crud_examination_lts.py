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
        db.add(db_obj)
        db.commit()
        return db_obj

examinationlts = CRUDExaminationLts(ExaminationLts)