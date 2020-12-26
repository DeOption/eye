from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.examination_tsj import ExaminationTsj
from app.snow.snowflake import worker
from typing import Any

class CRUDExaminationTsj(CRUDBase[None, ExaminationTsj, None]):
    def createExaminationTsj(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加同视机
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {examination_tsj_tss, examination_tsj_tss_sp, examination_tsj_tss_cz, examination_tsj_tss_cs_z}
        :return: None
        """
        examination_tsj_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = ExaminationTsj(
            base_info_id=base_info_id,
            examination_tsj_id=examination_tsj_id,
            **data
        )
        db.add(db_obj)
        db.commit()
        db.close()
        return db_obj

    def updateExaminationTsj(self, db: Session, id: str, data: dict) -> Any:
        """修改同视机"""
        data = jsonable_encoder(data)
        db.query(ExaminationTsj).filter(ExaminationTsj.base_info_id == id).update(data)
        db.commit()
        db.close()
        return None

examinationtsj = CRUDExaminationTsj(ExaminationTsj)