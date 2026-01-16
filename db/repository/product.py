from sqlalchemy.orm import Session
from db.models.product import Product
from schemas.product import CreateProduct, ShowProduct, UpdateProduct
from db.models.user import User
from datetime import datetime

def create_new_product(product:CreateProduct, by_user:User, db:Session):
    new_product = Product(
    product_name=product.product_name,
    sku_code = product.sku_code,
    description=product.description,
    category = product.category,
    status = product.status,
    price=product.price,
    stock = product.stock,
    tax=product.tax,

    owned_by=by_user.id,
    created_by=by_user.id,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return new_product


def get_all_products(db:Session):

    queryset = db.query(Product).filter().all()

    return queryset

def get_product_by_id(id:int, db:Session):
    product_in_db = db.query(Product).filter(Product.id == id).first()

    return product_in_db

def update_product_by_id(id:int, data:UpdateProduct, by_user:User, db:Session):
    product_in_db = db.query(Product).filter(Product.id == id).first()
    
    if product_in_db is None:
        return
    
    update_data = data.model_dump(exclude_unset=True)  # only provided keys
    
    for key, value in update_data.items():
        setattr(product_in_db, key, value)

    product_in_db.updated_at = datetime.now()
    product_in_db.updated_by = by_user.id
    
    db.add(product_in_db)
    db.commit()
    db.refresh(product_in_db)
    return product_in_db

def delete_product_by_id(id:int, db:Session):
    product_in_db = db.query(Product).filter(Product.id == id).first()
    if not product_in_db:
        return False
    db.delete(product_in_db)
    db.commit()
    return True   