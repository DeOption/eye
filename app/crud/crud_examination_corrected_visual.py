from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.examination_corrected_visual import ExaminationCorrectedVisual
from app.snow.snowflake import worker
from typing import Any

class CRUDExaminationCorrectedVisual(CRUDBase[None, ExaminationCorrectedVisual, None]):
    def createExaminationCorrectedVisual(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加矫正视力
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {left, right}
        :return: None
        """
        examination_corrected_visual_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = ExaminationCorrectedVisual(
            base_info_id=base_info_id,
            examination_corrected_visual_id=examination_corrected_visual_id,
            **data
        )

        return db_obj

    def updateExaminationCorrectedVisual(self, db: Session, id: str, data: dict) -> Any:
        """修改矫正视力"""
        data = jsonable_encoder(data)
        db.query(ExaminationCorrectedVisual).filter(ExaminationCorrectedVisual.base_info_id == id).update(data)

        return None

examinationcorrectedvisual = CRUDExaminationCorrectedVisual(ExaminationCorrectedVisual)