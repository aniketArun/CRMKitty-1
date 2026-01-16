from fastapi import Depends, APIRouter, status, HTTPException
from db.session import get_db
from sqlalchemy.orm import Session
from schemas.company import CreateCompany, ShowCompany, UpdateCompany
from db.models.user import User
from services.auth import get_current_user
from db.repository.company import get_all_companies, create_new_company, update_company_by_id


router = APIRouter()

@router.get("/")
def all_company(db:Session = Depends(get_db)):
    all_cp = get_all_companies(db=db)

    if all_cp is None:
        raise HTTPException(detail="No Company Found in DB!", status_code=status.HTTP_404_NOT_FOUND)
    return all_cp

@router.post("/", response_model=ShowCompany, status_code=status.HTTP_201_CREATED)
def create_company(cp:CreateCompany, db:Session = Depends(get_db)):
    new_cp = create_new_company(cp=cp, db=db)

    if new_cp is None:
        raise HTTPException(detail="Not able to crate Company", status_code=status.HTTP_406_NOT_ACCEPTABLE)
    return new_cp


@router.patch("/<id:int>", response_model=ShowCompany, status_code=status.HTTP_202_ACCEPTED)
def update_company_id(
        id:int, 
        data:UpdateCompany, 
        user:User = Depends(get_current_user),
        db:Session = Depends(get_db)
    ):
    
    updated_cp = update_company_by_id(id=id, data=data, user=user, db=db)
    if updated_cp is None:
        raise HTTPException(detail="Unable to update the Company", status_code=status.HTTP_406_NOT_ACCEPTABLE)
    
    return updated_cp