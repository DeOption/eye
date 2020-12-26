from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.examination_cornea import ExaminationCornea
from app.snow.snowflake import worker
from typing import Any

class CRUDExaminationCornea(CRUDBase[None, ExaminationCornea, None]):
    def createExaminationCornea(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加角膜荧光
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {eye_type, examination_cornea_sp, examination_cornea_cz, examination_cornea_cz_z}\n
        :return: None
        """
        examination_cornea_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = ExaminationCornea(
            base_info_id=base_info_id,
            examination_cornea_id=examination_cornea_id,
            **data
        )
        db.add(db_obj)
        db.commit()
        db.close()
        return db_obj

    def updateExaminationCornea(self, db: Session, id: str, data: dict) -> Any:
        """修改角膜映光"""
        data = jsonable_encoder(data)
        db.query(ExaminationCornea).filter(ExaminationCornea.base_info_id == id).update(data)
        db.commit()
        db.close()
        return None

examinationcornea = CRUDExaminationCornea(ExaminationCornea)