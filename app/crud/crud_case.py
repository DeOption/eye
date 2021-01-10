from typing import Any
from sqlalchemy.orm import Session
from sqlalchemy.sql import or_, and_
from app.crud.base import CRUDBase
from app.models.base_info import BaseInfo
from app.models.examination_lts import ExaminationLts
from app.models.examination_slj import ExaminationSlj
from app.models.diagnosis import Diagnosis
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

    def getCaseCondition(
            self,
            db: Session,
            age: str,
            id: str,
            id_number: str,
            examination_lts_j: str,
            examination_lts_y: str,
            examination_slj_zj_near: str,
            examination_slj_zj_far: str,
            examination_slj_dy_near: str,
            examination_slj_dy_far: str,
            examination_slj_cz: str,
            examination_slj_cz_z: str,
            k_method: str,
            latent_strabismus: bool,
            Internal_strabismus: str,
            Exotropia: str,
            A_V: str,
            V: str,
            S: str,
            PS: str,
            N: bool,
            other: bool,
            size: int,
            offset: int
    ) -> Any:
        """
        检索：通过年龄、立体视、三棱镜、诊断
        """
        base_info_list: list = []
        examination_lts_list: list = []
        examination_slj_list: list = []
        diagnosis_list: list = []

        if age:
            base_info_list.append(BaseInfo.age == age)
        if id:
            base_info_list.append(BaseInfo.id == id)
        if id_number:
            base_info_list.append(BaseInfo.id_number == id_number)
        if examination_lts_j:
            examination_lts_list.append(ExaminationLts.examination_lts_j == examination_lts_j)
        if examination_lts_y:
            examination_lts_list.append(ExaminationLts.examination_lts_y == examination_lts_y)
        if examination_slj_zj_near:
            examination_slj_list.append(ExaminationSlj.examination_slj_zj_near == examination_slj_zj_near)
        if examination_slj_zj_far:
            examination_slj_list.append(ExaminationSlj.examination_slj_zj_far == examination_slj_zj_far)
        if examination_slj_dy_near:
            examination_slj_list.append(ExaminationSlj.examination_slj_dy_near == examination_slj_dy_near)
        if examination_slj_dy_far:
            examination_slj_list.append(ExaminationSlj.examination_slj_dy_far == examination_slj_dy_far)
        if examination_slj_cz:
            examination_slj_list.append(ExaminationSlj.examination_slj_cz == examination_slj_cz)
        if examination_slj_cz_z:
            examination_slj_list.append(ExaminationSlj.examination_slj_cz_z ==examination_slj_cz_z)
        if k_method:
            examination_slj_list.append(ExaminationSlj.k_method == k_method)
        if latent_strabismus:
            diagnosis_list.append(Diagnosis.latent_strabismus == latent_strabismus)
        if Internal_strabismus:
            diagnosis_list.append(Diagnosis.Internal_strabismus == Internal_strabismus)
        if Exotropia:
            diagnosis_list.append(Diagnosis.Exotropia == Exotropia)
        if A_V:
            diagnosis_list.append(Diagnosis.A_V == A_V)
        if V:
            diagnosis_list.append(Diagnosis.V == V)
        if S:
            diagnosis_list.append(Diagnosis.S == S)
        if PS:
            diagnosis_list.append(Diagnosis.PS == PS)
        if N:
            diagnosis_list.append(Diagnosis.N == N)
        if other:
            diagnosis_list.append(Diagnosis.other == other)

        print(base_info_list, examination_slj_list, examination_lts_list, diagnosis_list)

        patient = db.query(BaseInfo).filter(*base_info_list).\
            outerjoin(ExaminationLts).filter(*examination_lts_list).\
            outerjoin(ExaminationSlj).filter(*examination_slj_list).\
            outerjoin(Diagnosis).filter(*diagnosis_list).\
            limit(size).offset((offset-1)*size).all()

        total = db.query(BaseInfo).filter(*base_info_list). \
            outerjoin(ExaminationLts).filter(*examination_lts_list). \
            outerjoin(ExaminationSlj).filter(*examination_slj_list). \
            outerjoin(Diagnosis).filter(*diagnosis_list).count()

        # patient_list: list = []
        # patient_dict: dict = {}
        # for patient_i in patient:
        #     patient_dict['base_info'] = {
        #         "id": patient_i.id,
        #         "data_type": patient_i.data_type,
        #         "user_name": patient_i.user_name,
        #         "sex": patient_i.sex,
        #         "age": patient_i.age,
        #         "id_number": patient_i.id_number,
        #         "phone_number": patient_i.phone_number,
        #         "order_number": patient_i.order_number,
        #         "create_time": patient_i.create_time,
        #         "modify_time": patient_i.modify_time,
        #         "suifang": patient_i.suifang,
        #         "beizhu": patient_i.beizhu
        #     }
            # patient_dict['medicalHistory'] = patient_i.medicalHistory[0] if patient_i.medicalHistory else ""
            # patient_dict['examinationNv'] = patient_i.examinationNv[0] if patient_i.examinationNv else ""
            # patient_dict['examinationCorrectedVisual'] = patient_i.examinationCorrectedVisual[0] if patient_i.examinationCorrectedVisual else ""
            # patient_dict['examinationCo'] = patient_i.examinationCo if patient_i.examinationCo else ""
            # patient_dict['examinationRo'] = patient_i.examinationRo if patient_i.examinationRo else ""
            # patient_dict['examinationTsj'] = patient_i.examinationTsj[0] if patient_i.examinationTsj else ""
            # patient_dict['examinationLts'] = patient_i.examinationLts[0] if patient_i.examinationLts else ""
            # patient_dict['examinationControl'] = patient_i.examinationControl[0] if patient_i.examinationControl else ""
            # patient_dict['examinationSlj'] = patient_i.examinationSlj[0] if patient_i.examinationSlj else ""
            # patient_dict['examinationEyeballsport'] = patient_i.examinationEyeballsport if patient_i.examinationEyeballsport else ""
            # patient_dict['diagnosis1'] = patient_i.diagnosis1[0] if patient_i.diagnosis1 else ""
            # patient_dict['surgery1'] = patient_i.surgery1[0] if patient_i.surgery1 else ""
            # patient_dict['leaveHospitalLts'] = patient_i.leaveHospitalLts[0] if patient_i.leaveHospitalLts else ""
            # patient_dict['leaveHospitalCornea'] = patient_i.leaveHospitalCornea[0] if patient_i.leaveHospitalCornea else ""
            # patient_dict['leaveHospitalSlj'] = patient_i.leaveHospitalSlj[0] if patient_i.leaveHospitalSlj else ""
            # patient_dict['leaveHospitalEyeballsport'] = patient_i.leaveHospitalEyeballsport if patient_i.leaveHospitalEyeballsport else ""
            # patient_dict['examinationCornea'] = patient_i.examinationCornea if patient_i.examinationCornea else ""
            # patient_list.append(patient_dict)
            # patient_dict = {}

        return [patient, total]


    def getCaseDetail(

            self,
            db: Session,
            id: str,
            size: int,
            offset: int
    ) -> list:
        """
        获取病例详情
        :param db: 数据库连接对象
        :param id_number: 患者身份证号
        :return: ...
        """
        patient = db.query(BaseInfo).filter(BaseInfo.id == id).limit(size).offset((offset-1)*size).all()
        total = db.query(BaseInfo).filter(BaseInfo.id == id).count()
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
            patient_dict['medicalHistory'] = patient_i.medicalHistory[0] if patient_i.medicalHistory else ""
            patient_dict['examinationNv'] = patient_i.examinationNv[0] if patient_i.examinationNv else ""
            patient_dict['examinationCorrectedVisual'] = patient_i.examinationCorrectedVisual[0] if patient_i.examinationCorrectedVisual else ""
            patient_dict['examinationCo'] = patient_i.examinationCo if patient_i.examinationCo else ""
            patient_dict['examinationRo'] = patient_i.examinationRo if patient_i.examinationRo else ""
            patient_dict['examinationTsj'] = patient_i.examinationTsj[0] if patient_i.examinationTsj else ""
            patient_dict['examinationLts'] = patient_i.examinationLts[0] if patient_i.examinationLts else ""
            patient_dict['examinationControl'] = patient_i.examinationControl[0] if patient_i.examinationControl else ""
            patient_dict['examinationSlj'] = patient_i.examinationSlj[0] if patient_i.examinationSlj else ""
            patient_dict['examinationEyeballsport'] = patient_i.examinationEyeballsport if patient_i.examinationEyeballsport else ""
            patient_dict['diagnosis1'] = patient_i.diagnosis1[0] if patient_i.diagnosis1 else ""
            patient_dict['surgery1'] = patient_i.surgery1[0] if patient_i.surgery1 else ""
            patient_dict['leaveHospitalLts'] = patient_i.leaveHospitalLts[0] if patient_i.leaveHospitalLts else ""
            patient_dict['leaveHospitalCornea'] = patient_i.leaveHospitalCornea[0] if patient_i.leaveHospitalCornea else ""
            patient_dict['leaveHospitalSlj'] = patient_i.leaveHospitalSlj[0] if patient_i.leaveHospitalSlj else ""
            patient_dict['leaveHospitalEyeballsport'] = patient_i.leaveHospitalEyeballsport if patient_i.leaveHospitalEyeballsport else ""
            patient_dict['examinationCornea'] = patient_i.examinationCornea if patient_i.examinationCornea else ""
            patient_list.append(patient_dict)
            # patient_dict = {}

        return [patient_dict, total]

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