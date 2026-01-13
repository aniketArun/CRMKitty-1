from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from db.repository.customer import create_new_customer, get_all_customers
from schemas.customer import CreateCustomer, ShowCustomer
from typing import List
router = APIRouter()

@router.post("/", response_model=ShowCustomer, status_code=status.HTTP_201_CREATED)
def create_customer(customer:CreateCustomer, db:Session = Depends(get_db)):
    new_customer = create_new_customer(customer=customer, db=db)

    if new_customer is None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Not able to create Customer!")
    return new_customer

@router.get("/", response_model=List[ShowCustomer], status_code=status.HTTP_200_OK)
def all_customers(db:Session = Depends(get_db)):
    customers = get_all_customers(db=db)

    if customers is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Customers Found, Create One!")
    return customers

