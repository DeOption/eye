from typing import Any
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.base_info import BaseInfo


class CRUDCase(CRUDBase[None, BaseInfo, None]):
    """
        通过uid获取病例列表
    """

    def getCaseLists(
            self,
            db: Session,
            id_number: str,
            size: int,
            offset: int
    ) -> Any:
        """
        通过身份证号查询病例信息
        :param db: 数据库连接对象
        :param id_number: 患者身份证号
        :return: 所有患者的信息
        """
        return db.query(BaseInfo).filter(BaseInfo.id_number == id_number).limit(size).offset((offset-1)*size).all()

    def getAllCaseLists(
            self,
            db: Session,
            size: int,
            offset: int
    ):
        """
        获取全部病例信息
        :param db: 数据库连接对象
        :return: 所有患者信息
        """
        return db.query(BaseInfo).limit(size).offset((offset-1)*size).all()


case = CRUDCase(BaseInfo)
