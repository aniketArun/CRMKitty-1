from db.models.invoice import Invoice
from sqlalchemy.orm import Session
from schemas.invoice import CreateInvoice, ShowInvoice, UpdateInvoice
from db.models.user import User
from datetime import datetime

def create_new_invoice(invoice:CreateInvoice, by_user:User, db:Session):
    new_invoice = Invoice(
        company_id = invoice.company_id,
        invoice_date = invoice.invoice_date,
        customer_id = invoice.customer_id,
        due_date = invoice.due_date,
        discount = invoice.discount,
        paymt_method = invoice.paymt_method,
        status = invoice.status,
        notes = invoice.notes,
        items = invoice.items,

        created_by = by_user.id,
    )

    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)

    return new_invoice


def get_all_invoices(user:User, db:Session):
    queryset = db.query(Invoice).filter(Invoice.company_id == user.company_id).all()

    return queryset


def get_invoice_by_id(id:int, db:Session):
    inv_in_db = db.query(Invoice).filter(Invoice.id == id).first()
    return inv_in_db

def update_invoice_by_id(id:int, data:UpdateInvoice, by_user:User, db:Session):
    inv_in_db = db.query(Invoice).filter(Invoice.id==id).first()
    if inv_in_db is None:
        return
    
    update_data = inv_in_db.model_dump(exclude_unset=True)  # only provided keys
    
    for key, value in update_data.items():
        setattr(inv_in_db, key, value)

    inv_in_db.updated_at = datetime.now()
    inv_in_db.updated_by = by_user.id
    
    db.add(inv_in_db)
    db.commit()
    db.refresh(inv_in_db)
    return inv_in_db


def delete_invoice_by_id(id:int, db:Session):
    invoice = db.query(Invoice).filter(Invoice.id == id).first()
    if not invoice:
        return False
    db.delete(invoice)
    db.commit()
    return True

