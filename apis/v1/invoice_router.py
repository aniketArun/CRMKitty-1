from db.session import get_db
from fastapi import APIRouter, status, HTTPException, Depends
from schemas.invoice import CreateInvoice, ShowInvoice, UpdateInvoice
from sqlalchemy.orm import Session
from db.repository.invoice import create_new_invoice, get_all_invoices, get_invoice_by_id
from typing import List
from fastapi_pagination import Page, paginate
from services.auth import get_current_user
from db.models.user import User
router = APIRouter()

@router.post("/", response_model=ShowInvoice, status_code=status.HTTP_201_CREATED)
def create_invoice(invoice:CreateInvoice, db:Session = Depends(get_db)):
    new_invoice = create_new_invoice(invoice=invoice, db=db)

    if new_invoice is None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Not able to create new Invoice!")
    return new_invoice


@router.get("/", response_model=Page[ShowInvoice], status_code=status.HTTP_200_OK)
def all_invoices(db:Session = Depends(get_db)):
    invoices = get_all_invoices(db=db)

    if invoices is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Invoices Found!")
    return paginate(invoices)


@router.get("/<id:int>", response_model=ShowInvoice, status_code=status.HTTP_200_OK)
def get_invoice(id:int, user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    invoice = get_invoice_by_id(db=db)

    if invoice is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No Invoice Found! with id {id}")
    return paginate(invoice)

@router.put("/<id:int>",response_model=ShowInvoice)
def update_invoice(id:int, data:UpdateInvoice, by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    pass
