from services.auth import create_access_token, authenticate_user, get_current_user
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from core.config import settings
from db.session import get_db
from core.hashing import Hasher
from db.repository.login import get_user_by_email
from jose import jwt, JWTError

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

