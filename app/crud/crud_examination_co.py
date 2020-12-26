from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.examination_co import ExaminationCo
from app.snow.snowflake import worker
from typing import Any

class CRUDExaminationCo(CRUDBase[None, ExaminationCo, None]):
    def createExaminationCo(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加电脑验光
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {eye_type, ds, dc, a}
        :return: None
        """
        examination_co_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = ExaminationCo(
            base_info_id=base_info_id,
            examination_co_id=examination_co_id,
            **data
        )
        db.add(db_obj)
        db.commit()
        db.close()
        return db_obj

    def updateExaminationCo(self, db: Session, id: str, data: dict) -> Any:
        """修改电脑验光"""
        data = jsonable_encoder(data)
        db.query(ExaminationCo).filter(ExaminationCo.base_info_id == id).update(data)
        db.commit()
        db.close()
        return None

examinationco = CRUDExaminationCo(ExaminationCo)