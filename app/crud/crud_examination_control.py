from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.examination_control import ExaminationControl
from app.snow.snowflake import worker
from typing import Any

class CRUDExaminationControl(CRUDBase[None, ExaminationControl, None]):
    def createExaminationControl(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加眼球运动
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: examination_control
        :return: None
        """
        examination_control_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = ExaminationControl(
            base_info_id=base_info_id,
            examination_control_id=examination_control_id,
            examination_Control=data
        )

        return db_obj

    def updateExaminationControl(self, db: Session, id: str, data: dict) -> Any:
        """修改控制力"""
        data = jsonable_encoder(data)
        print(data)
        db.query(ExaminationControl).filter(ExaminationControl.base_info_id == id).update({"examination_Control": data})

        return None

examinationcontrol = CRUDExaminationControl(ExaminationControl)