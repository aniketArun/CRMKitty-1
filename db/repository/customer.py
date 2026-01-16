from sqlalchemy.orm import Session
from db.models.customer import Customer
from schemas.customer import CreateCustomer, ShowCustomer, UpdateCustomer
from db.models.user import User
from datetime import datetime

def create_new_customer(customer:CreateCustomer, by_user:User, db:Session):
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
        created_by = by_user.id
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


def get_all_customers(db:Session):
    queryset = db.query(Customer).filter().all()

    return queryset

def get_customer_by_id(id:int, db:Session):
    customer_in_db = db.query(Customer).filter(Customer.id == id).first()

    return customer_in_db

def update_cust_by_id(id:int, data:UpdateCustomer, by_user:User, db:Session):
    cust_in_db  = db.query(Customer).filter(Customer.id == id).first()

    if cust_in_db is None:
        return
    update_data = data.model_dump(exclude_unset=True)  # only provided keys
    
    for key, value in update_data.items():
        setattr(cust_in_db, key, value)

    cust_in_db.updated_at = datetime.now()
    cust_in_db.updated_by = by_user.id
    
    db.add(cust_in_db)
    db.commit()
    db.refresh(cust_in_db)
    return cust_in_db