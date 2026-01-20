from sqlalchemy.orm import Session
from db.models.report import Report
from schemas.report import CreateReport, UpdateReport
from db.models.user import User
from datetime import datetime

def create_new_report(report:CreateReport, db:Session):
    new_report = Report(
        company_id=report.company_id,
        title = report.title,
        customer_id = report.customer_id,
        report_summary = report.report_summary,
        test_cases = report.test_cases,
        remarks = report.remarks,
        status = report.status
    )

    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return new_report



def get_all_report(user:User, db:Session):

    queryset = db.query(Report).filter(Report.company_id == user.company_id).all()

    return queryset

def get_report_by_id(id:int, db:Session):
    report_in_db = db.query(Report).filter(Report.id == id).first()

    return report_in_db

def update_report_by_id(id:int, data:UpdateReport, by_user:User, db:Session):
    rp_in_db = db.query(Report).filter(Report.id == id).first()
    
    if rp_in_db is None:
        return
    
    update_data = data.model_dump(exclude_unset=True)  # only provided keys
    
    for key, value in update_data.items():
        setattr(rp_in_db, key, value)

    rp_in_db.updated_at = datetime.now()
    rp_in_db.updated_by = by_user.id
    
    db.add(rp_in_db)
    db.commit()
    db.refresh(rp_in_db)
    return rp_in_db

def delete_report_by_id(id:int, db:Session):
    rp_in_db = db.query(Report).filter(Report.id == id).first()
    if not rp_in_db:
        return False
    db.delete(rp_in_db)
    db.commit()
    return True   

