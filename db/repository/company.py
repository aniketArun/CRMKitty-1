from sqlalchemy.orm import Session
from db.models.company import Company

def get_company_from_user_id(id:int, db:Session):
    cp = db.query(Company).filter(id = id).first()

    return cp