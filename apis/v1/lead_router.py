from fastapi import APIRouter, HTTPException, status, Depends
from schemas.lead import CreateLead,ShowLead
from sqlalchemy.orm import Session
from db.repository.leads import create_new_lead, show_all_leads
from db.session import get_db
from typing import List


router = APIRouter()


@router.post("/", response_model=ShowLead, status_code=status.HTTP_201_CREATED)
def create_lead(lead:CreateLead, db:Session=Depends(get_db)):
    new_lead = create_new_lead(lead=lead, db = db)

    if new_lead is not None:
        return lead
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Not Able to Create Lead!")

@router.get("/", response_model=List[ShowLead], status_code=status.HTTP_200_OK)
def show_leads(db:Session=Depends(get_db)):
    leads = show_all_leads(db = db)

    if not leads:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No leads Fount!")
    return leads