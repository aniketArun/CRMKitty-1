from db.session import get_db
from fastapi import APIRouter, status, HTTPException, Depends
from schemas.invoice import CreateInvoice, ShowInvoice, UpdateInvoice
from sqlalchemy.orm import Session
from db.repository.invoice import (
    create_new_invoice, 
    get_all_invoices, 
    get_invoice_by_id, 
    update_invoice_by_id, 
    delete_invoice_by_id
)
from typing import List
from fastapi_pagination import Page, paginate
from services.auth import get_current_user, require_permission
from db.models.user import User
from core.enums import Permission

router = APIRouter()

@router.post(
        "/", 
        response_model=ShowInvoice, 
        status_code=status.HTTP_201_CREATED,
        dependencies=[Depends(require_permission(Permission.INVOICE_CREATE))]
        )
def create_invoice(invoice:CreateInvoice, user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    new_invoice = create_new_invoice(invoice=invoice, db=db, by_user = user)

    if new_invoice is None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Not able to create new Invoice!")
    return new_invoice


@router.get(
        "/", 
        response_model=Page[ShowInvoice], 
        status_code=status.HTTP_200_OK,
        dependencies=[Depends(require_permission(Permission.INVOICE_READ))]
        )
def all_invoices(user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    invoices = get_all_invoices(user = user, db=db)

    if invoices is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Invoices Found!")
    return paginate(invoices)


@router.get(
        "/<id:int>", 
        response_model=ShowInvoice, 
        status_code=status.HTTP_200_OK,
        dependencies=[Depends(require_permission(Permission.INVOICE_READ))]
        )
def get_invoice(id:int, user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    invoice = get_invoice_by_id(id=id, db=db)

    if invoice is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No Invoice Found! with id {id}")
    return paginate(invoice)

@router.put(
        "/<id:int>",
        response_model=ShowInvoice, 
        status_code=status.HTTP_202_ACCEPTED,
        dependencies=[Depends(require_permission(Permission.INVOICE_UPDATE))]
        )
def update_invoice(id:int, data:UpdateInvoice, by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    invoice_updated = update_invoice_by_id(id=id, data=data, by_user=by_user, db=db)

    if invoice_updated is None:
        raise HTTPException(detail="Invoie Update Failed!", status_code=status.HTTP_406_NOT_ACCEPTABLE)
    return invoice_updated


@router.delete("/<id:int>", status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(require_permission(Permission.INVOICE_DELETE))])
def delete_invoice(id:int, by_user: User = Depends(get_current_user), db:Session = Depends(get_db)):
    invoice_deleted = delete_invoice_by_id(id=id, db=db)

    if invoice_deleted:
        return {"Mesaage":"invoice deleted!"}
    raise HTTPException(detail="No Invoice Found or Something went Wrong", status_code=status.HTTP_404_NOT_FOUND)
