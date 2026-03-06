from sqlalchemy.orm import Session
from db.models.lead import Lead
from db.models.user import User
from schemas.lead import CreateLead, UpdateLead
from .activity_log import create_log
from datetime import datetime

from core.enums import Status

def get_lead_by_id(id:int, db:Session):
    lead_in_db = db.query(Lead).filter(Lead.id == id).first()

    return lead_in_db

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
    create_log(
        db, 
        description=f"Lead Created {new_lead.first_name}", 
        created_by = created_by_user.id,
        lead_id = new_lead.id,
        company_id = created_by_user.company_id
        )
    return new_lead


def update_lead_by_id(id:int, lead: UpdateLead, db: Session, by_user:User):
    lead_in_db:Lead = db.query(Lead).filter(Lead.id==id).first()
    if lead_in_db is None:
        return
    
    update_data = lead.model_dump(exclude_unset=True)  # only provided keys
    
    for key, value in update_data.items():
        setattr(lead_in_db, key, value)

    lead_in_db.updated_at = datetime.now()
    lead_in_db.updated_by = by_user.id
    
    db.add(lead_in_db)
    db.commit()
    db.refresh(lead_in_db)
    create_log(
        db, 
        description=f"Lead Updated {lead_in_db.first_name}", 
        created_by = by_user.id,
        lead_id = lead_in_db.id,
        company_id = by_user.company_id
        )
    return lead_in_db



def show_all_leads(user:User, db:Session):

    all_leads = db.query(Lead).filter(Lead.owned_by == user.company_id).all()

    return all_leads


def delete_lead_by_id(id:int,db:Session, by_user:User):
    lead:Lead = db.query(Lead).filter(Lead.id == id).first()
    if not lead:
        return False
    db.delete(lead)
    db.commit()
    create_log(
        db, 
        description=f"Lead Deleted {lead.first_name}", 
        created_by = by_user.id,
        company_id = by_user.company_id
        )
    return True
