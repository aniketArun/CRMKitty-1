from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from db.repository.customer import create_new_customer, get_all_customers, get_customer_by_id, update_cust_by_id
from schemas.customer import CreateCustomer, ShowCustomer, UpdateCustomer
from typing import List
from fastapi_pagination import Page, add_pagination, paginate
from db.models.user import User
from services.auth import get_current_user


router = APIRouter()


@router.get("/<id:int>", response_model=ShowCustomer, status_code=status.HTTP_200_OK)
def get_customer(id:int, user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    customer = get_customer_by_id(id= id, db=db)

    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Customer Found, Create One!")
    return customer



@router.post("/", response_model=CreateCustomer, status_code=status.HTTP_201_CREATED)
def create_customer(customer:CreateCustomer, db:Session = Depends(get_db), user:User = Depends(get_current_user)):
    new_customer = create_new_customer(customer=customer, db=db, by_user = user)

    if new_customer is None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Not able to create Customer!")
    return new_customer


@router.get("/", response_model=Page[ShowCustomer], status_code=status.HTTP_200_OK)
def all_customers(db:Session = Depends(get_db)):
    customers = get_all_customers(db=db)

    if customers is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Customers Found, Create One!")
    return paginate(customers)

@router.put("/<id:int>", response_model=ShowCustomer, status_code=status.HTTP_202_ACCEPTED)
def update_customer(id:int, data:UpdateCustomer, by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    cust_updated = update_cust_by_id(id=id, data=data, by_user=by_user, db=db)

    if cust_updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Customers Found, Create One!")
    return cust_updated

