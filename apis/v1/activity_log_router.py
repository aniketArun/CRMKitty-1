from fastapi import APIRouter, status, HTTPException, Depends
from schemas.activity_log import ActivityLog
from db.repository.activity_log import get_logs_for_user
from db.session import get_db
from sqlalchemy.orm import Session
from db.models.user import User
from services.auth import get_current_user
from fastapi_pagination import paginate, Page

router = APIRouter()


@router.get("/me", response_model=Page[ActivityLog], status_code=status.HTTP_200_OK)
def my_activity(by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    act = get_logs_for_user(user=by_user, db=db)
    if act is None:
        raise HTTPException(detail="No Activity", status_code=status.HTTP_404_NOT_FOUND)
    return paginate(act)