from sqlalchemy.orm import Session
from db.models.lead import Lead
from schemas.lead import CreateLead

from fastapi import HTTPException, status
from datetime import datetime

from core.enums import Status


def create_new_lead(lead: CreateLead, db: Session):
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
        created_by=lead.created_by,
        created_at=lead.created_at if lead.created_at else datetime.now(),
        updated_at=lead.updated_at
    )
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)
    return new_lead



def show_all_leads(db:Session):

    all_leads = db.query(Lead).filter().all()

    return all_leads