from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.examination_eyeballsport import ExaminationEyeballsport
from app.snow.snowflake import worker
from typing import Any

class CRUDExaminationEyeballsport(CRUDBase[None, ExaminationEyeballsport, None]):
    def createExaminationEyeballsport(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加眼球运动
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {eye_type, normal, external_rectus, internal_rectus, pper_rectus, lower_rectus, upper_oblique, lower_oblique}\n
        :return: None
        """
        examination_eyeballsport_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = ExaminationEyeballsport(
            base_info_id=base_info_id,
            examination_eyeballsport_id=examination_eyeballsport_id,
            **data
        )
        db.add(db_obj)
        db.commit()
        db.close()
        return db_obj

    def updateExaminationEyeballsport(self, db: Session, id: str, data: dict) -> Any:
        """修改眼球运动"""
        data = jsonable_encoder(data)
        db.query(ExaminationEyeballsport).filter(ExaminationEyeballsport.base_info_id == id).update(data)
        db.commit()
        db.close()
        return None

examinationeyeballsport = CRUDExaminationEyeballsport(ExaminationEyeballsport)