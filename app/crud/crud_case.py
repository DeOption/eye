from typing import Any
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.base_info import BaseInfo
from app.models.examination_lts import ExaminationLts
from fastapi.encoders import jsonable_encoder
import datetime
import re


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
        caseList = db.query(BaseInfo).filter(BaseInfo.id_number == id_number).limit(size).offset((offset-1)*size).all()
        total = db.query(BaseInfo).filter(BaseInfo.id_number == id_number).all()
        return caseList, total
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
        caseList = db.query(BaseInfo).limit(size).offset((offset-1)*size).all()
        total = db.query(BaseInfo).all()
        return caseList, total

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
        db.close()
        return db_obj

    def getCaseByLts(
            self,
            db: Session,
            age: str,
            examination_lts_j: str,
            examination_lts_y: str
    ) -> Any:
        """
        检索：通过年龄、立体视、三棱镜、诊断
        """
        print(age)
        a = db.query(BaseInfo).filter(BaseInfo.age.like("%"+age+"%")).join(ExaminationLts).filter(ExaminationLts.examination_lts_j == examination_lts_j, ExaminationLts.examination_lts_y == examination_lts_y).all()
        return a


    def getCaseDetail(
            self,
            db: Session,
            id_number: str,
            size: int,
            offset: int
    ) -> list:
        """
        获取病例详情
        :param db: 数据库连接对象
        :param id_number: 患者身份证号
        :return: ...
        """
        patient = db.query(BaseInfo).filter(BaseInfo.id_number == id_number).limit(size).offset((offset-1)*size).all()
        total = db.query(BaseInfo).filter(BaseInfo.id_number == id_number).all()
        patient_list: list = []
        patient_dict: dict = {}
        for patient_i in patient:
            patient_dict['base_info'] = {
                "id": patient_i.id,
                "data_type": patient_i.data_type,
                "user_name": patient_i.user_name,
                "sex": patient_i.sex,
                "age": patient_i.age,
                "id_number": patient_i.id_number,
                "phone_number": patient_i.phone_number,
                "order_number": patient_i.order_number,
                "create_time": patient_i.create_time,
                "modify_time": patient_i.modify_time,
                "suifang": patient_i.suifang,
                "beizhu": patient_i.beizhu
            }
            patient_dict['medicalHistory'] = patient_i.medicalHistory[0]
            patient_dict['examinationNv'] = patient_i.examinationNv[0]
            patient_dict['examinationCorrectedVisual'] = patient_i.examinationCorrectedVisual[0]
            patient_dict['examinationCo'] = patient_i.examinationCo[0]
            patient_dict['examinationRo'] = patient_i.examinationRo[0]
            patient_dict['examinationTsj'] = patient_i.examinationTsj[0]
            patient_dict['examinationLts'] = patient_i.examinationLts[0]
            patient_dict['examinationControl'] = patient_i.examinationControl[0]
            patient_dict['examinationSlj'] = patient_i.examinationSlj[0]
            patient_dict['examinationEyeballsport'] = patient_i.examinationEyeballsport[0]
            patient_dict['diagnosis1'] = patient_i.diagnosis1[0]
            patient_dict['surgery1'] = patient_i.surgery1[0]
            patient_dict['leaveHospitalLts'] = patient_i.leaveHospitalLts[0]
            patient_dict['leaveHospitalCornea'] = patient_i.leaveHospitalCornea[0]
            patient_dict['leaveHospitalSlj'] = patient_i.leaveHospitalSlj[0]
            patient_dict['leaveHospitalEyeballsport'] = patient_i.leaveHospitalEyeballsport[0]
            patient_dict['examinationCornea'] = patient_i.examinationCornea[0]
            patient_list.append(patient_dict)
            patient_dict = {}

        return patient_list, total

    def updateBaseInfoDetails(self, db: Session, id: str, data: dict) -> Any:
        """修改病例详情"""
        data = jsonable_encoder(data)
        db.query(BaseInfo).filter(BaseInfo.id == id).update(data)
        db.commit()
        db.close()
        return None


case = CRUDCase(BaseInfo)

if __name__ == '__main__':
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(create_time)