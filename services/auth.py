from core.hashing import Hasher
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.enums import Role
from db.repository.login import get_user_by_email
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from db.session import get_db
from core.config import settings
from datetime import datetime, timedelta

def authenticate_user(email:str, password:str, db:Session):
    user = get_user_by_email(email = email, db = db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password=password, hashed=user.password):
        return False
    return user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/token')

def get_current_user(token:str = Depends(oauth2_scheme), db:Session = Depends(get_db)):
    credentials_excepetion = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Could not vaidate the token"
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email:str = payload.get("sub")
        if email is None:
            raise credentials_excepetion
    except:
        raise credentials_excepetion
    user = get_user_by_email(email = email, db = db)
    if user is None:
        raise credentials_excepetion
    return user



def create_access_token(data:dict):
    to_encode = data.copy()


    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MIN)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return encoded_jwt


def require_permission(permission: str):
    async def dependency(user = Depends(get_current_user)):
        # user.role is a single Role object
        if not user.role or not user.role.permissions:
            raise HTTPException(
                status_code=403,
                detail="No role or permissions assigned"
            )
      
        # Grant full access if role is admin 
        if user.role.name == Role.ADMIN.value:
            return

        if permission not in user.role.permissions:
            raise HTTPException(
                status_code=403,
                detail=f"Permission '{permission}' required"
            )
    return dependency

