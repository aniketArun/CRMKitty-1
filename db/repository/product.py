from sqlalchemy.orm import Session
from db.models.product import Product
from schemas.product import CreateProduct, ShowProduct


def create_new_product(product:CreateProduct, db:Session):
    new_product = Product(
    product_name=product.product_name,
    sku_code = product.sku_code,
    description=product.description,
    category = product.category,
    status = product.status,
    price=product.price,
    stock = product.stock,
    tax=product.tax,

    owned_by=product.owned_by,
    created_by=product.created_by,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return new_product


def get_all_products(db:Session):

    queryset = db.query(Product).filter().all()

    return queryset