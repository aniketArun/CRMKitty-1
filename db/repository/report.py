from sqlalchemy.orm import Session
from db.models.report import Report
from schemas.report import CreateReport


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



def get_all_report(db:Session):

    queryset = db.query(Report).filter().all()

    return queryset


