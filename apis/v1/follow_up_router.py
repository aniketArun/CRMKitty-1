from fastapi import APIRouter, status, HTTPException, Depends
from db.models.follow_up import FollowUp
from schemas.follow_up import CreateFollowUp, ShowFollowUp, UpdateFollowUp
from db.session import get_db
from sqlalchemy.orm import Session
from db.models.user import User
from db.repository.follow_up import get_upcoming_follow_ups, create_new_follow_up
from services.auth import get_current_user
from fastapi_pagination import paginate, Page

router = APIRouter()


@router.get("/", response_model=Page[ShowFollowUp], status_code=status.HTTP_200_OK)
def get_all_follow_ups(by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    follow_ups = get_upcoming_follow_ups(by_user=by_user, db = db)

    if follow_ups is None:
        raise HTTPException(detail="No Follow-ups scheduled for you!", status_code=status.HTTP_404_NOT_FOUND)
    return paginate(follow_ups)

@router.post("/", response_model=ShowFollowUp, status_code=status.HTTP_201_CREATED)
def create_follow_up(data:CreateFollowUp ,by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    follow_up_created = create_new_follow_up(data=data, by_user=by_user, db=db)
    
    if follow_up_created is None:
        raise HTTPException (detail="Failed to create new Follow-up!", status_code=status.HTTP_406_NOT_ACCEPTABLE)
    return follow_up_created