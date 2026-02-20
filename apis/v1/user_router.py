from fastapi import APIRouter, HTTPException, status, Depends
from schemas.user import CreateUser,ShowUser, UpdateUser
from db.models.user import User
from sqlalchemy.orm import Session
from db.repository.user import (
    create_new_user, 
    show_all_users,
    update_current_user,
    update_user_by_id, 
    get_user_by_id,
    delete_user_by_id
    )
from db.session import get_db
from core.enums import Permission
from typing import List
from services.auth import get_current_user, require_permission

router = APIRouter()

@router.post(
    "/", 
    response_model=ShowUser, 
    status_code=status.HTTP_201_CREATED, 
    dependencies=[Depends(require_permission(Permission.USER_CREATE))]
    )
def create_user(user:CreateUser, db:Session=Depends(get_db)):
    try:
        new_user = create_new_user(user=user, db = db)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.get(
    "/", 
    response_model=List[ShowUser], 
    status_code=status.HTTP_200_OK, 
    dependencies=[Depends(require_permission(Permission.USER_READ))]
)
def show_users(user:User = Depends(get_current_user),db:Session=Depends(get_db)):
    users = show_all_users(user=user, db=db)
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found!")
    
    return users

@router.patch("/me", response_model=ShowUser, status_code=status.HTTP_202_ACCEPTED)
def update_my_profile(user:UpdateUser, by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    updated_user = update_current_user(data=user, user=by_user, db=db)

    if updated_user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Updated failed")
    return updated_user

@router.put(
        "/{id}", 
        response_model=ShowUser, 
        status_code=status.HTTP_202_ACCEPTED, 
        dependencies=[Depends(require_permission(Permission.USER_UPDATE))]
        )
def update_user(id:int, user:UpdateUser, by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    updated_user = update_user_by_id(id=id, data=user, db=db)

    if updated_user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Updated failed")
    return updated_user

@router.get("/{id}", response_model=ShowUser, status_code=status.HTTP_200_OK)
def get_user(id:int, by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    user_in_db = get_user_by_id(id=id, db=db)
    if user_in_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user Found!")
    return user_in_db

@router.delete(
        "/{id}", 
        status_code=status.HTTP_200_OK,
        dependencies=[Depends(require_permission(Permission.USER_DELETE))]
        )
def delete_user(id:int, by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    user_in_db = delete_user_by_id(id=id, db=db)
    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user Found!")
    return {"message":"user deleted !"}