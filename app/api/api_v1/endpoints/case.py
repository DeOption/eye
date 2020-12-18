from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from typing import Optional
from app.crud import crud_case, crud_user
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
    :return: {
            "return_msg": "OK",\n
            "case_list": [],\n
            "total": "\n
            }
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
