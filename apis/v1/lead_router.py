from fastapi import APIRouter, HTTPException, status, Depends, Response
from schemas.lead import CreateLead,ShowLead, UpdateLead
from sqlalchemy.orm import Session
from db.repository.leads import create_new_lead, show_all_leads, update_lead_by_id, get_lead_by_id, delete_lead_by_id
from db.session import get_db
from typing import List
from services.auth import get_current_user
from db.models.user import User
from fastapi_pagination import Page, add_pagination, paginate


router = APIRouter()

@router.get("/", response_model=Page[ShowLead], status_code=status.HTTP_200_OK)
def show_leads(db:Session=Depends(get_db), user:User = Depends(get_current_user)):
    leads = show_all_leads(db = db)

    if not leads:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No leads Fount!")
    return paginate(leads)


@router.post("/", response_model=ShowLead, status_code=status.HTTP_201_CREATED)
def create_lead(lead:CreateLead, db:Session=Depends(get_db), user:User = Depends(get_current_user)):
    new_lead = create_new_lead(lead=lead, db = db, created_by_user= user)
    if new_lead is not None:
        return new_lead
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Not Able to Create Lead!")



@router.patch("/<id:int>", response_model=ShowLead, status_code=status.HTTP_202_ACCEPTED)
def update_lead(
    id:int, 
    data:UpdateLead, 
    db:Session = Depends(get_db), 
    user:User = Depends(get_current_user)
    ):
    db_lead = update_lead_by_id(id=id, lead=data, db=db, by_user=user)
    if db_lead is None:
        raise HTTPException(detail="Something Went Wrong Not able to update the lead", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return db_lead


@router.get("/<id:int>", response_model=ShowLead, status_code=status.HTTP_202_ACCEPTED)
def get_lead(
    id:int, 
    db:Session = Depends(get_db), 
    user:User = Depends(get_current_user)
    ):
    db_lead = get_lead_by_id(id=id, db=db)
    if db_lead is None:
        raise HTTPException(detail=f"No lead fount with id {id}", status_code=status.HTTP_404_NOT_FOUND)
    return db_lead


@router.delete("/<id:int>", status_code=status.HTTP_202_ACCEPTED)
def delete_lead(
    id:int, 
    db:Session = Depends(get_db), 
    user:User = Depends(get_current_user)
    ):
    db_lead = delete_lead_by_id(id=id, db=db)
    if db_lead is False:
        raise HTTPException(detail=f"No lead fount with id {id}", status_code=status.HTTP_404_NOT_FOUND)
    return Response({"Message":"Lead Deleted succesfully !"}, status_code=status.HTTP_202_ACCEPTED)