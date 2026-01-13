from db.models.invoice import Invoice
from sqlalchemy.orm import Session
from schemas.invoice import CreateInvoice, ShowInvoice


def create_new_invoice(invoice:CreateInvoice, db:Session):
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

        created_by = invoice.created_by,
        updated_at = invoice.updated_at
    )

    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)

    return new_invoice


def get_all_invoices(db:Session):
    queryset = db.query(Invoice).filter().all()

    return queryset

