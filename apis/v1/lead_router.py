from fastapi import APIRouter, HTTPException, status, Depends, Response
from schemas.lead import CreateLead,ShowLead, UpdateLead
from sqlalchemy.orm import Session
from db.repository.leads import (
    create_new_lead, 
    show_all_leads, 
    update_lead_by_id, 
    get_lead_by_id, 
    delete_lead_by_id
    )
from db.session import get_db
from typing import List
from services.auth import get_current_user, require_permission
from db.models.user import User
from fastapi_pagination import Page, add_pagination, paginate
from core.enums import Permission
import json

router = APIRouter()

@router.get(
        "/", 
        response_model=Page[ShowLead], 
        status_code=status.HTTP_200_OK,
        dependencies=[Depends(require_permission(Permission.LEAD_READ))]
        )
def show_leads(db:Session=Depends(get_db), user:User = Depends(get_current_user)):
    leads = show_all_leads(user=user, db = db)

    if not leads:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No leads Fount!")
    return paginate(leads)


@router.post(
        "/", 
        response_model=ShowLead, 
        status_code=status.HTTP_201_CREATED,
        dependencies=[Depends(require_permission(Permission.LEAD_CREATE))]
        )
def create_lead(lead:CreateLead, db:Session=Depends(get_db), user:User = Depends(get_current_user)):
    new_lead = create_new_lead(lead=lead, db = db, created_by_user= user)
    if new_lead is not None:
        return new_lead
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Not Able to Create Lead!")



@router.patch("/{id}", response_model=ShowLead, status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(require_permission(Permission.LEAD_UPDATE))])
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


@router.get("/{id}", response_model=ShowLead, status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(require_permission(Permission.LEAD_READ))])
def get_lead(
    id:int, 
    db:Session = Depends(get_db), 
    user:User = Depends(get_current_user)
    ):
    db_lead = get_lead_by_id(id=id, db=db)
    if db_lead is None:
        raise HTTPException(detail=f"No lead fount with id {id}", status_code=status.HTTP_404_NOT_FOUND)
    return db_lead


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(require_permission(Permission.LEAD_DELETE))])
def delete_lead(
    id:int, 
    db:Session = Depends(get_db), 
    user:User = Depends(get_current_user)
    ):
    db_lead = delete_lead_by_id(id=id, db=db)
    if db_lead is False:
        raise HTTPException(detail=f"No lead fount with id {id}", status_code=status.HTTP_404_NOT_FOUND)
    return Response( 
        content=json.dumps({"Message": "Lead Deleted successfully!"}), 
        status_code=status.HTTP_202_ACCEPTED, 
        media_type="application/json" 
        )