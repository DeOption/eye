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
        examination_ro_id_left = worker.get_id()
        examination_ro_id_right = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = [
            ExaminationRo(
                base_info_id=base_info_id,
                examination_ro_id=examination_ro_id_left,
                eye_type="left",
                **data["left"]
            ),
            ExaminationRo(
                base_info_id=base_info_id,
                examination_ro_id=examination_ro_id_right,
                eye_type="right",
                **data["right"]
            )
        ]

        return db_obj

    def updateExaminationRo(self, db: Session, id: str, data: dict) -> Any:
        """修改检影验光"""
        data = jsonable_encoder(data)
        db.query(ExaminationRo).\
            filter(ExaminationRo.base_info_id == id, ExaminationRo.eye_type == "left").\
            update(data["left"])
        db.query(ExaminationRo).\
            filter(ExaminationRo.base_info_id == id, ExaminationRo.eye_type == "right").\
            update(data["right"])

        return None

examinationro = CRUDExaminationRo(ExaminationRo)