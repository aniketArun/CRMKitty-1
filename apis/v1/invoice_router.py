from db.session import get_db
from fastapi import APIRouter, status, HTTPException, Depends
from schemas.invoice import CreateInvoice, ShowInvoice
from sqlalchemy.orm import Session
from db.repository.invoice import create_new_invoice, get_all_invoices
from typing import List
from fastapi_pagination import Page, paginate

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