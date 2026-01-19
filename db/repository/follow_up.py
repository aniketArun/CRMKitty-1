from sqlalchemy.orm import Session
from schemas.follow_up import CreateFollowUp,UpdateFollowUp, ShowFollowUp
from db.models.user import User
from db.models.follow_up import FollowUp


def get_upcoming_follow_ups(by_user:User, db:Session):
    queryset = db.query(FollowUp).filter(FollowUp.created_by == by_user.id).all()

    return queryset

def create_new_follow_up(data:CreateFollowUp, by_user:User, db:Session):
    new_follow_up = FollowUp(
    title = data.title,
    description = data.description,
    follow_date = data.follow_date,
    lead_id = data.lead_id,
    customer_id = data.customer_id,
    user_id = data.user_id,
    created_by = by_user.id,
    )
    db.add(new_follow_up)
    db.commit()
    db.refresh(new_follow_up)
    return new_follow_up

