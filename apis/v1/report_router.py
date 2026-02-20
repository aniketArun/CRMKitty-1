from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from schemas.report import CreateReport, ShowReport, UpdateReport
from db.repository.report import (
    create_new_report, 
    get_all_report, 
    get_report_by_id, 
    delete_report_by_id, 
    update_report_by_id
)
from db.session import get_db
from typing import List
from fastapi_pagination import paginate, Page
from db.models.user import User
from services.auth import get_current_user, require_permission
from core.enums import Permission
import json

router = APIRouter()

@router.post(
        "/", 
        response_model=ShowReport, 
        status_code=status.HTTP_201_CREATED,
        dependencies=[Depends(require_permission(Permission.REPORT_CREATE))]
        )
def create_report(report:CreateReport, db:Session = Depends(get_db)):
    new_report = create_new_report(report=report, db=db)

    if new_report is None:
        raise HTTPException(detail="Failed to create new report", status_code=status.HTTP_406_NOT_ACCEPTABLE)
    
    # Explicitly convert to ShowReport 
    return new_report

@router.get(
        "/", 
        response_model=Page[ShowReport], 
        status_code=status.HTTP_200_OK,
        dependencies=[Depends(require_permission(Permission.REPORT_READ))]
        )
def all_reports(db:Session = Depends(get_db), user:User = Depends(get_current_user)):

    reports = get_all_report(user=user, db=db)

    if reports is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Reports Found!")
    
    return paginate(reports)

@router.get(
        "/{id}", 
        response_model=ShowReport, 
        status_code=status.HTTP_200_OK,
        dependencies=[Depends(require_permission(Permission.REPORT_READ))]
        )
def get_report_from_id(id:int, by_user:User= Depends(get_current_user), db:Session = Depends(get_db)):
    report_in_db = get_report_by_id(id=id, db=db)

    if report_in_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Report Found!")  
    return report_in_db 

@router.put(
        "/{id}", 
        response_model=ShowReport, 
        status_code=status.HTTP_202_ACCEPTED,
        dependencies=[Depends(require_permission(Permission.REPORT_UPDATE))]
        )
def update_report(id:int, data:UpdateReport, by_user:User= Depends(get_current_user), db:Session = Depends(get_db)):
    report_updated = update_report_by_id(id=id, data=data, by_user=by_user, db=db)

    if report_updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Report Found!")  
    return report_updated      


@router.delete(
        "/{id}", 
        status_code=status.HTTP_202_ACCEPTED,
        dependencies=[Depends(require_permission(Permission.REPORT_DELETE))]
        )
def delete_report(id:int, by_user:User= Depends(get_current_user), db:Session = Depends(get_db)):
    report = delete_report_by_id(id=id, by_user=by_user, db=db)

    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Report Found!")  
    return Response(content=json.dumps({"message":"Report Deleted!"}), status_code=status.HTTP_200_OK, media_type="application/json")