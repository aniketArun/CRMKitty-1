from fastapi import APIRouter, Depends, status, HTTPException
from db.repository.role import create_new_role, get_all_role
from db.session import get_db
from sqlalchemy.orm import Session
from schemas.role import CreateRole, ShowRole
from services.auth import get_current_user, require_permission
from fastapi_pagination import paginate, Page
from core.enums import Permission
router = APIRouter()

@router.post(
        "/", 
        response_model=ShowRole, 
        status_code=status.HTTP_201_CREATED,
        dependencies=[Depends(require_permission(Permission.ROLE_CREATE))]
        )
def create_role(role:CreateRole, db:Session = Depends(get_db)):
    new_role = create_new_role(role=role, db=db)

    if new_role is None:
        raise HTTPException(detail="Not able to create new role!", status_code=status.HTTP_406_NOT_ACCEPTABLE)
    
    return new_role

@router.get(
        "/", 
        response_model=Page[ShowRole], 
        status_code=status.HTTP_200_OK,
        dependencies=[Depends(require_permission(Permission.ROLE_READ))]
        )
def get_role(db:Session = Depends(get_db)):
    all_roles = get_all_role(db=db)

    if all_roles is None:
        raise HTTPException(detail="No role have been created!", status_code=status.HTTP_404_NOT_FOUND)
    
    return paginate(all_roles)

