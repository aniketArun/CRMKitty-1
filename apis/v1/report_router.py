from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas.report import CreateReport, ShowReport
from db.repository.report import create_new_report, get_all_report
from db.session import get_db
from typing import List


router = APIRouter()

@router.post("/", response_model=ShowReport, status_code=status.HTTP_201_CREATED)
def create_report(report:CreateReport, db:Session = Depends(get_db)):
    new_report = create_new_report(report=report, db=db)

    if new_report is None:
        raise HTTPException(detail="Failed to create new report", status_code=status.HTTP_406_NOT_ACCEPTABLE)
    
    return new_report

@router.get("/", response_model=List[ShowReport], status_code=status.HTTP_200_OK)
def all_reports(db:Session = Depends(get_db)):

    reports = get_all_report(db=db)

    if reports is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Reports Found!")
    
    return reports
