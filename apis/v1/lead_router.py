from fastapi import APIRouter, HTTPException, status, Depends
from schemas.lead import CreateLead,ShowLead
from sqlalchemy.orm import Session
from db.repository.leads import create_new_lead, show_all_leads
from db.session import get_db
from typing import List
from services.auth import get_current_user
from db.models.user import User
from fastapi_pagination import Page, add_pagination, paginate


router = APIRouter()


@router.post("/", response_model=ShowLead, status_code=status.HTTP_201_CREATED)
def create_lead(lead:CreateLead, db:Session=Depends(get_db), user:User = Depends(get_current_user)):
    new_lead = create_new_lead(lead=lead, db = db, created_by_user= user)
    if new_lead is not None:
        return new_lead
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Not Able to Create Lead!")

@router.get("/", response_model=Page[ShowLead], status_code=status.HTTP_200_OK)
def show_leads(db:Session=Depends(get_db)):
    leads = show_all_leads(db = db)

    if not leads:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No leads Fount!")
    return paginate(leads)