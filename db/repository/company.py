from sqlalchemy.orm import Session
from db.models.company import Company
from schemas.company import CreateCompany


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


