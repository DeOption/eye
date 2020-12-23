from fastapi import APIRouter, Depends, Query, Body, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from typing import Optional
from app.crud import crud_case, crud_medical_history, crud_diagnosis, crud_surgery, crud_examination_nv, crud_examination_corrected_visual, crud_examination_co, crud_examination_ro, crud_examination_tsj, crud_examination_lts, crud_examination_cornea, crud_examination_slj, crud_examination_eyeballsport, crud_examination_control, crud_leave_hospital_lts, crud_leave_hospital_slj, crud_leave_hospital_cornea, crud_leave_hospital_eyeballsport
from app.snow.snowflake import worker

router = APIRouter()


@router.get('/get_case_list', summary="获取病例列表")
def getCaseList(
        db: Session = Depends(deps.get_db),
        id_number: Optional[str] = Query(None, description='患者身份证号'),
        size: Optional[int] = Query(None, description="页面大小"),
        offset: Optional[int] = Query(None, description="当前页码")
) -> dict:
    """
    接口：获取病例列表，医生通过输入患者的身份证号，查询出具体患者的病例信息\n
    :param db: 数据库连接对象\n
    :param id_number: 患者的身份证号/如果身份证号不填写，返回所有病例信息\n
    :param size: 页面大小\n
    :param offset: 当前页码\n
    :return: {\n
            "return_msg": "OK",\n
            "case_list": [],\n
            "total": "\n
    }\n
    """
    if id_number:
        caselist = crud_case.case.getCaseLists(db=db, id_number=id_number, size=size, offset=offset)
        if not caselist:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="没有此病例！"
            )
    else:
        caselist = crud_case.case.getAllCaseLists(db=db, size=size, offset=offset)
    return {
        "return_msg": "OK",
        "case_list": caselist,
        "total": len(caselist)
    }


@router.post('/submit_case_content', summary="提交病例")
def submitCaseContent(
        db: Session = Depends(deps.get_db),
        base_info: Optional[dict] = Body(..., description="基本信息"),
        medical_history: Optional[dict] = Body(..., description="病史"),
        examination: Optional[dict] = Body(..., description="检查"),
        diagnosis: Optional[dict] = Body(..., description="诊断"),
        surgery: Optional[dict] = Body(..., description="手术设计"),
        leave_history: Optional[dict] = Body(..., description="出院情况"),
) -> dict:
    """
    提交病例信息\n
    :param db: 数据库对象\n
    :param base_info: 基本信息\n
        {data_type, user_name, sex, age, id_number, phone_number, order_number, suifang, beizhu}\n
        {数据类别，姓名，性别，年龄，身份证号，手机号，登记号，随访，备注}\n
    :param medical_history: \n
        {surgery_history, glasses_history, amblyopia_history, home_history, born_history, surgery_history_edit, now_age, now_wt, now_fs}\n
        {手术史，眼镜史，弱视治疗史，家族史，生产史，手术史补充，斜视年龄，歪头，复视}\n
    :param examination: \n
        {examination_nv, examination_corrected_visual, examination_co, examination_ro, examination_tsj, examination_lts, examination_cornea, examination_slj, examination_eyeballsport, examination_control}\n
        examination_nv: dict #裸眼视力\n
            {left, right}\n
        examination_corrected_visual: dict #矫正视力\n
            {left, right}\n
        examination_co: dict #电脑验光\n
            {eye_type, ds, dc, a}\n
        examination_ro: dict #检影验光\n
            {eye_type, ds, dc, a}\n
        examination_tsj: dict #同视机\n
            {examination_tsj_tss, examination_tsj_tss_sp, examination_tsj_tss_cz, examination_tsj_tss_cs_z}\n
            {同时视，同时视水平值，同时视垂直值，同时视垂直值具体数值}\n
        examination_lts: dict #立体视\n
            {examination_lts_j, examination_lts_y}\n
            {近方随机点立体视，远方随机点立体视}\n
        examination_cornea: dict #角膜映光\n
            {eye_type, examination_cornea_sp, examination_cornea_cz, examination_cornea_cz_z}\n
            {眼别，水平值，垂直值，垂直数值}\n
        examination_slj: dict #三棱镜\n
            {examination_slj_zj_near, examination_slj_zj_far, examination_slj_dy_near, examination_slj_dy_far, examination_slj_cz, examination_slj_cz_z, k_method}\n
            {视近(直角)，视远(直角)，视近(等腰)，视远(等腰)，垂直三棱镜，0-50，k法}\n
        examination_eyeballsport: dict #眼球运动\n
            {eye_type, normal, external_rectus, internal_rectus, pper_rectus, lower_rectus, upper_oblique, lower_oblique}\n
            {眼别，正常，外直肌，内直肌，上直肌，下直肌，上斜肌，下斜肌}\n
        examination_control: str #控制力\n
    :param diagnosis: #诊断\n
        {latent_strabismus, Internal_strabismus, Exotropia, A_V, V, S, PS, N, other}\n
        {隐斜视，内斜视，外斜视，A⁃V斜视，垂直旋转性斜视，特殊类型斜视，中枢性麻痹性斜视，眼球震颤，其他}\n
    :param surgery: #手术设计\n
        {surgery_yb, muscle, way, value, beizhu}\n
        {手术设计眼别，肌肉，方式，量值，备注}\n
    :param leave_history: #出院时情况\n
        {leave_hospital_lts, leave_hospital_cornea, leave_hospital_slj, leave_hospital_eyeballsport}\n
        {立体视（出院），角膜映光（出院），三棱镜（出院），眼球运动（出院）}\n
        leave_hospital_lts: dict #立体视（出院）\n
            {examination_lts_j, examination_lts_y}\n
            {近方随机点立体视，远方随机点立体视}\n
        leave_hospital_slj: dict #三棱镜（出院）\n
            {leave_hospital_slj_near, leave_hospital_slj_far}\n
            {视近，视远}\n
        leave_hospital_cornea: dict #角膜映光（出院）\n
            {examination_cornea_sp, examination_cornea_cz, examination_cornea_cz_z}\n
            {水平值，垂直值，垂直数值}\n
        leave_hospital_eyeballsport: dict #眼球运动（出院）\n
            {eye_type, normal, external_rectus, internal_rectus, pper_rectus, lower_rectus, upper_oblique, lower_oblique}\n
            {眼别，正常，外直肌，内直肌，上直肌，下直肌，上斜肌，下斜肌}\n
    :return: 提交成功返回200/ok
    """


    id = worker.get_id() #病例id
    crud_case.case.createBaseInfo(db=db, id=id, data=base_info)
    crud_medical_history.medicalhistory.createMedicalHistory(db=db, base_info_id=id, data=medical_history)

    crud_examination_nv.examinationnv.createExaminationNv(db=db, base_info_id=id, data=examination['examination_nv'])
    crud_examination_corrected_visual.examinationcorrectedvisual.createExaminationCorrectedVisual(db=db, base_info_id=id, data=examination['examination_corrected_visual'])
    crud_examination_co.examinationco.createExaminationCo(db=db, base_info_id=id, data=examination['examination_co'])
    crud_examination_ro.examinationro.createExaminationRo(db=db, base_info_id=id, data=examination['examination_ro'])
    crud_examination_tsj.examinationtsj.createExaminationTsj(db=db, base_info_id=id, data=examination['examination_tsj'])
    crud_examination_lts.examinationlts.createExaminationLts(db=db, base_info_id=id, data=examination['examination_lts'])
    crud_examination_cornea.examinationcornea.createExaminationCornea(db=db, base_info_id=id, data=examination['examination_cornea'])
    crud_examination_slj.examinationslj.createExaminationSlj(db=db, base_info_id=id, data=examination['examination_slj'])
    crud_examination_eyeballsport.examinationeyeballsport.createExaminationSlj(db=db, base_info_id=id, data=examination['examination_eyeballsport'])
    crud_examination_control.examinationcontrol.createExaminationControl(db=db, base_info_id=id, data=examination['examination_control'])

    crud_leave_hospital_lts.leavehospitallts.createLeaveHospitalLts(db=db, base_info_id=id, data=leave_history['leave_hospital_lts'])
    crud_leave_hospital_slj.leavehospitalslj.createLeaveHospitalSlj(db=db, base_info_id=id, data=leave_history['leave_hospital_slj'])
    crud_leave_hospital_cornea.leavehospitalcornea.createLeaveHospitalCornea(db=db, base_info_id=id, data=leave_history['leave_hospital_cornea'])
    crud_leave_hospital_eyeballsport.leavehospitaleyeballsport.createLeaveHospitalEyeballsport(db=db, base_info_id=id, data=leave_history['leave_hospital_eyeballsport'])

    crud_diagnosis.diagnosis.createDiagnosis(db=db, base_info_id=id, data=diagnosis)
    crud_surgery.surgery.createSurgery(db=db, base_info_id=id, data=surgery)



    return {"return_msg": "OK"}

if __name__ == '__main__':
    id = worker.get_id()
    print(id)