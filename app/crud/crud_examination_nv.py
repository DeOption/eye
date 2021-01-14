from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.examination_nv import ExaminationNv
from app.snow.snowflake import worker
from typing import Any

class CRUDExaminationNv(CRUDBase[None, ExaminationNv, None]):
    def createExaminationNv(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加裸眼视力
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {left, right}
        :return: None
        """
        examination_nv_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = ExaminationNv(
            base_info_id=base_info_id,
            examination_nv_id=examination_nv_id,
            **data
        )

        return db_obj

    def updateExaminationNv(self, db: Session, id: str, data: dict) -> Any:
        """修改裸眼视力"""
        data = jsonable_encoder(data)
        db.query(ExaminationNv).filter(ExaminationNv.base_info_id == id).update(data)

        return None

examinationnv = CRUDExaminationNv(ExaminationNv)