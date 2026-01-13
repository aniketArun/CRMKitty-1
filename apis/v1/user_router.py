from fastapi import APIRouter, HTTPException, status, Depends
from schemas.user import CreateUser,ShowUser
from sqlalchemy.orm import Session
from db.repository.user import create_new_user, show_all_users
from db.session import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user:CreateUser, db:Session=Depends(get_db)):
    new_user = create_new_user(user=user, db = db)
    if new_user is None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Not able to create User")

    return new_user


@router.get("/", response_model=List[ShowUser], status_code=status.HTTP_200_OK)
def show_users(db:Session=Depends(get_db)):
    users = show_all_users(db=db)
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found!")
    
    return users
    