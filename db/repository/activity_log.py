from sqlalchemy.orm import Session
from db.models.activity_log import ActivityLog
from db.models.user import User


def get_logs_for_user(user:User, db:Session):
    query_set = db.query(ActivityLog).filter(ActivityLog.created_by == user.id).all()
    return query_set