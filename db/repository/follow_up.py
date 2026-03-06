from sqlalchemy.orm import Session
from schemas.follow_up import CreateFollowUp,UpdateFollowUp, ShowFollowUp
from db.models.user import User
from db.models.follow_up import FollowUp
from .activity_log import create_log

def get_upcoming_follow_ups(by_user:User, db:Session):
    queryset = db.query(FollowUp).filter(FollowUp.created_by == by_user.id).all()

    return queryset

def create_new_follow_up(data:CreateFollowUp, by_user:User, db:Session):
    _data = data.model_dump(exclude_unset=True)  # only provided keys
    
    new_follow_up = FollowUp(
    title = data.title,
    follow_date = data.follow_date,
    )
    for key, value in _data.items():
        setattr(new_follow_up, key, value)
    db.add(new_follow_up)
    db.commit()
    db.refresh(new_follow_up)
    create_log(
        db=db,
        description= f"Follow up {new_follow_up.title} is created",
        created_by = by_user.id,
        follow_up_id = new_follow_up.id,
        company_id = by_user.company_id,
        lead_id = new_follow_up.lead_id,
        customer_id = new_follow_up.customer_id,
        user_id = new_follow_up.user_id
        )
    return new_follow_up

