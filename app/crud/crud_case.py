from typing import Any

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.base_info import BaseInfo
from app.models.base_ref import BaseRef


class CRUDCase(CRUDBase[BaseRef, BaseInfo, None]):
    """
        通过uid获取病例列表
    """
    def getCaseLists(
            self,
            db: Session,
            uid: str,
            # is_admin: bool
    ) -> Any:
        baseref = db.query(BaseRef).filter(BaseRef.uid == uid).first()
        baseinfo = db.query(BaseInfo).filter(BaseInfo.uid == uid).first()
        # return baseref.base_infos[0]
        return {
            "id": baseref.uid,
            "user_name": baseinfo.name,
            "create_time": baseref.create_time,
            "modify_time": baseref.modify_time,
        }


case = CRUDCase(BaseRef)