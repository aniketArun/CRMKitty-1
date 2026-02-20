from services.auth import (
    create_access_token, 
    authenticate_user, 
    get_current_user, 
    require_permission
    )
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from core.config import settings
from db.session import get_db
from db.repository.user import get_user_by_id
from db.models.user import User
from db.repository.login import get_user_by_email
from jose import jwt, JWTError
from schemas.user import ShowUser
from core.enums import Permission
from schemas.login import LoginForm
router = APIRouter()

@router.post("/token")
def login_for_access_token(form_data:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            detail="Incoreect email or password",
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    access_token = create_access_token(data = {"sub":user.email})
    return {"access_token":access_token, "token_type":"bearer"}

@router.get("/me", response_model=ShowUser, status_code=status.HTTP_200_OK)
def get_me(user = Depends(get_current_user)):
    if user is None:
        raise HTTPException(detail="Not able to find user with the assocaited token", status_code=status.HTTP_404_NOT_FOUND)
    return user

@router.post("/impersonate/<user_id:int>", dependencies=[Depends(require_permission(Permission.IMPERSONITION))])
def impersonate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # Find the target user by ID
    target_user = get_user_by_id(id=user_id, db=db)
    if not target_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Target user not found"
        )

    # Create token with impersonation flag
    access_token = create_access_token(
        data={
            "sub": str(target_user.email),          # subject is user ID now
            "impersonated_by": str(current_user.id)
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "impersonated_user_id": target_user.id
    }
