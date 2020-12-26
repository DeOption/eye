from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.examination_slj import ExaminationSlj
from app.snow.snowflake import worker
from typing import Any

class CRUDExaminationSlj(CRUDBase[None, ExaminationSlj, None]):
    def createExaminationSlj(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加三棱镜
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {examination_slj_zj_near, examination_slj_zj_far, examination_slj_dy_near, examination_slj_dy_far, examination_slj_cz, examination_slj_cz_z, k_method}\n
        :return: None
        """
        examination_slj_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = ExaminationSlj(
            base_info_id=base_info_id,
            examination_slj_id=examination_slj_id,
            **data
        )
        db.add(db_obj)
        db.commit()
        db.close()
        return db_obj

    def updateExaminationSlj(self, db: Session, id: str, data: dict) -> Any:
        """修改三棱镜"""
        data = jsonable_encoder(data)
        db.query(ExaminationSlj).filter(ExaminationSlj.base_info_id == id).update(data)
        db.commit()
        db.close()
        return None



examinationslj = CRUDExaminationSlj(ExaminationSlj)

