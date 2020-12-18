from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from typing import Optional
from app.crud import crud_case
from app.models.base_ref import BaseRef
router = APIRouter()


@router.get('/get_case_list', summary="获取病例列表")
def getCaseList(
        db: Session = Depends(deps.get_db),
        uid: Optional[str] = Query(None, description='用户id')
) -> dict:
    """

    :param db:
    :param uid:
    :return:
    """

    caselist = crud_case.case.getCaseLists(db=db, uid=uid)
    if not caselist:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="没有此病例！"
        )

    return {
        "return_msg": "OK",
        "case_list": caselist
    }
