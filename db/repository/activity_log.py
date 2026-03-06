from sqlalchemy.orm import Session
from db.models.activity_log import ActivityLog
from db.models.user import User


def get_logs_for_user(user:User, db:Session):
    query_set = db.query(ActivityLog).filter(ActivityLog.created_by == user.id).all()
    return query_set

def create_log(db:Session, description, **kwrgs):

    _log = ActivityLog(description = description)
    for key, value in kwrgs.items():
        _log.__setattr__(key, value)
    db.add(_log)
    db.commit()
    db.refresh(_log)