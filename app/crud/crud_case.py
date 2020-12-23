from typing import Any
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.base_info import BaseInfo
from fastapi.encoders import jsonable_encoder
import datetime


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

    def createBaseInfo(
            self,
            db: Session,
            id: str,
            data: dict
    ) -> Any:
        """
        向 base_info 表中插入数据
        :param db: 数据库连接对象
        :param id: 病例ID
        :param data: [data_type, user_name, sex, age, id_number, phone_number, order_number, suifang, beizhu]
        :return: None
        """
        data = jsonable_encoder(data)
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db_obj = BaseInfo(
            id=id,
            create_time=time,
            modify_time=time,
            **data
        )
        db.add(db_obj)
        db.commit()
        return db_obj




case = CRUDCase(BaseInfo)

if __name__ == '__main__':
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(create_time)