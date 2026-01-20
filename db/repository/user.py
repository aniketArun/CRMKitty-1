from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.models.user import User
from schemas.user import CreateUser, UpdateUser
from fastapi import HTTPException, status
from datetime import datetime
from core.enums import Role
from core.hashing import Hasher

def create_new_user(user:CreateUser, db:Session)->User:
    '''
    Docstring for create_new_user
    
    :param user: Description
    :type user: CreateUser
    :param db: Description
    :type db: Session
    '''
    try:
        new_user = User(
            first_name=user.first_name, 
            last_name=user.last_name, 
            email=user.email, 
            mobile=user.mobile, 
            location=user.location, 
            role_id=user.role if user.role else Role.LEAD_MANAGER.value, 
            avatar=user.avatar, 
            created_at=datetime.now(), 
            password = Hasher.get_password_hashed(password=user.password),
            is_active=True 
        )
    
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError: 
        raise ValueError("User creation failed")


def show_all_users(user:User, db:Session):
    '''
    Docstring for show_all_users
    
    :param db: Description
    :type db: Session
    '''
    all_users = db.query(User).filter(User.company_id == user.company_id).all()

    return all_users


def get_user_by_id(id:int, db:Session):
    user = db.query(User).filter(User.id == id).first()
    return user

def update_current_user(data:UpdateUser, user:User, db:Session):
    if user is None:
        return
    
    update_data = data.model_dump(exclude_unset=True)  # only provided keys
    
    for key, value in update_data.items():
        setattr(user, key, value)

    user.updated_at = datetime.now()
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user_by_id(id:int, data:UpdateUser, db:Session):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        return
    
    update_data = data.model_dump(exclude_unset=True)  # only provided keys
    
    for key, value in update_data.items():
        setattr(user, key, value)

    user.updated_at = datetime.now()
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user