from sqlalchemy.orm import Session
from db.models.activity_log import ActivityLog
from db.models.user import User


def get_logs_for_user(user:User, db:Session):
    query_set = db.query(ActivityLog).filter(ActivityLog.created_by == user.id).all()
    return query_set

def get_logs_for_site(user:User, db:Session):
    query_set = db.query(ActivityLog).filter(ActivityLog.company_id == user.company_id).all()
    return query_set

def create_log(db:Session, description, **kwrgs):

    _log = ActivityLog(description = description)
    for key, value in kwrgs.items():
        _log.__setattr__(key, value)
    db.add(_log)
    db.commit()
    db.refresh(_log)

def get_logs_for_customer(id:int, db:Session):
    query_set = db.query(ActivityLog).filter(ActivityLog.customer_id == id).all()
    return query_set

def get_logs_for_lead(id:int, db:Session):
    query_set = db.query(ActivityLog).filter(ActivityLog.lead_id == id).all()
    return query_set

def get_logs_for_product(id:int, db:Session):
    query_set = db.query(ActivityLog).filter(ActivityLog.product_id == id).all()
    return query_set

def get_logs_for_invoice(id:int, db:Session):
    query_set = db.query(ActivityLog).filter(ActivityLog.invoice_id == id).all()
    return query_set

def get_logs_for_report(id:int, db:Session):
    query_set = db.query(ActivityLog).filter(ActivityLog.report_id == id).all()
    return query_set

def get_logs_for_one_user(id:int, db:Session):
    query_set = db.query(ActivityLog).filter(ActivityLog.created_by == id).all()
    return query_set

def get_logs_for_profile(id:int, db:Session):
    query_set = db.query(ActivityLog).filter(ActivityLog.user_id == id).all()
    return query_set