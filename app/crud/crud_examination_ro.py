from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.examination_ro import ExaminationRo
from app.snow.snowflake import worker
from typing import Any

class CRUDExaminationRo(CRUDBase[None, ExaminationRo, None]):
    def createExaminationRo(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加剑影验光
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {eye_type, ds, dc, a}
        :return: None
        """
        examination_ro_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = ExaminationRo(
            base_info_id=base_info_id,
            examination_ro_id=examination_ro_id,
            **data
        )
        db.add(db_obj)
        db.commit()
        return db_obj

examinationro = CRUDExaminationRo(ExaminationRo)