from sqlalchemy.orm import Session
from db.models.lead import Lead
from db.models.user import User
from schemas.lead import CreateLead

from fastapi import HTTPException, status
from datetime import datetime

from core.enums import Status


def create_new_lead(lead: CreateLead, db: Session, created_by_user:User):
    new_lead = Lead(
        first_name=lead.first_name,
        last_name=lead.last_name,
        dob=lead.dob,
        email=lead.email,
        phone=lead.phone,
        company=lead.company,
        source=lead.source,
        status=lead.status if lead.status else Status.NEW.name,
        lead_value=lead.lead_value,
        notes=lead.notes,
        refered_by=lead.refered_by,
        created_by=created_by_user.id,
        owned_by = created_by_user.company_id,
        created_at=lead.created_at if lead.created_at else datetime.now(),
        updated_at=lead.updated_at
    )
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)
    return new_lead


def update_lead_by_id(id:int, lead: CreateLead, db: Session, by_user:User):
    lead_in_db = db.query(Lead).filter(Lead.id==id).first()
    if lead_in_db is None:
        return
    
    lead_in_db.first_name=lead.first_name,
    lead_in_db.last_name=lead.last_name,
    lead_in_db.dob=lead.dob,
    lead_in_db.email=lead.email,
    lead_in_db.phone=lead.phone,
    lead_in_db.company=lead.company,
    lead_in_db.source=lead.source,
    lead_in_db.status=lead.status if lead.status else Status.NEW.name,
    lead_in_db.lead_value=lead.lead_value,
    lead_in_db.notes=lead.notes,
    lead_in_db.refered_by=lead.refered_by,
    lead_in_db.created_at=lead.created_at if lead.created_at else datetime.now(),
    lead_in_db.updated_at=lead.updated_at if lead.updated_at else datetime.now()
    
    db.add(lead_in_db)
    db.commit()
    db.refresh(lead_in_db)
    return lead_in_db



def show_all_leads(db:Session):

    all_leads = db.query(Lead).filter().all()

    return all_leads