from sqlalchemy.orm import Session
from db.models.company import Company
from schemas.company import UpdateCompany, CreateCompany
from db.models.user import User
from datetime import datetime
def get_company_from_user_id(id:int, db:Session):
    cp = db.query(Company).filter(id = id).first()

    return cp


def create_new_company(cp:CreateCompany, db:Session):
    new_cp = Company(
    name = cp.name,
    email= cp.email,
    phone = cp.phone,
    logo = cp.logo,
    currency = cp.currency,
    timezone = cp.timezone,

    billing_email = cp.billing_email,
    tax_id = cp.tax_id,
    billing_address = cp.billing_address,

    created_at = cp.created_at,
    updated_at = cp.updated_at,
    updated_by = cp.updated_by,
    plan_id = cp.plan_id,
    license_id = cp.license_id
    )

    db.add(new_cp)
    db.commit()
    db.refresh(new_cp)

    return new_cp


def get_all_companies(db:Session):
    queryset = db.query(Company).filter().all()
    return queryset

def update_company_by_id(id: int, user: User, data: UpdateCompany, db: Session):
    cp_in_db = db.query(Company).filter(Company.id == id).first()
    if cp_in_db is None:
        return None
    
    update_data = data.model_dump(exclude_unset=True)  # only provided keys
    
    for key, value in update_data.items():
        setattr(cp_in_db, key, value)

    cp_in_db.updated_at = datetime.now()
    cp_in_db.updated_by = user.id

    db.add(cp_in_db)
    db.commit()
    db.refresh(cp_in_db)

    return cp_in_db
