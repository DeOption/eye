from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.surgery import Surgery
from app.snow.snowflake import worker
from typing import Any

class CRUDSurgery(CRUDBase[None, Surgery, None]):
    def createSurgery(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加手术设计
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {surgery_history, glasses_history, amblyopia_history, home_history, born_history, surgery_history_edit, now_age, now_wt, now_fs}
        :return: None
        """
        surgery_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = Surgery(
            base_info_id=base_info_id,
            surgery_id=surgery_id,
            **data
        )
        db.add(db_obj)
        db.commit()
        db.close()
        return db_obj

    def updateSurgery(self, db: Session, id: str, data: dict) -> Any:
        """修改病例详情"""
        data = jsonable_encoder(data)
        db.query(Surgery).filter(Surgery.base_info_id == id).update(data)
        db.commit()
        db.close()
        return None

surgery = CRUDSurgery(Surgery)