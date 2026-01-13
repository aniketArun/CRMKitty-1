from sqlalchemy.orm import Session
from db.models.customer import Customer
from schemas.customer import CreateCustomer, ShowCustomer


def create_new_customer(customer:CreateCustomer, db:Session):
    new_customer = Customer(
        first_name = customer.first_name,
        last_name = customer.last_name,
        email = customer.email,
        phone = customer.phone,
        company = customer.company,
        category = customer.category,
        assigned_user_id = customer.assigned_user_id,
        addrees = customer.addrees,
        is_active = customer.is_active,
        created_by = customer.created_by
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


def get_all_customers(db:Session):
    queryset = db.query(Customer).filter().all()

    return queryset