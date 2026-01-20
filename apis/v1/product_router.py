from fastapi import APIRouter, Depends, status, HTTPException, Response
from schemas.product import CreateProduct, ShowProduct, UpdateProduct
from db.repository.product import (
    create_new_product, 
    get_all_products, 
    delete_product_by_id, 
    update_product_by_id,
    get_product_by_id
    )
from db.session import get_db
from sqlalchemy.orm import Session
from typing import List
from db.models.user import User
from services.auth import get_current_user, require_permission
from core.enums import Permission

router = APIRouter()

@router.get(
        "/", 
        response_model=List[ShowProduct], 
        status_code=status.HTTP_200_OK,
        dependencies=[Depends(require_permission(Permission.PRODUCT_READ))]
        )
def all_products(db:Session = Depends(get_db), user:User = Depends(get_current_user), ):
    products = get_all_products(user=user, db=db)

    if products is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Product have been created!")

    return products

@router.post(
        "/", 
        response_model=ShowProduct, 
        status_code=status.HTTP_201_CREATED,
        dependencies=[Depends(require_permission(Permission.PRODUCT_CREATE))]
        )
def create_product(product:CreateProduct, db:Session = Depends(get_db), by_user:User = Depends(get_current_user)):
    new_product = create_new_product(product=product, by_user = by_user, db=db)

    if new_product is None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Failed to create new Product!")
    
    return new_product

@router.get(
        "/<id:int>", 
        response_model=ShowProduct, 
        status_code=status.HTTP_200_OK,
        dependencies=[Depends(require_permission(Permission.PRODUCT_READ))]
        )
def get_product(id:int, user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    product = get_product_by_id(id= id, db=db)

    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Product Found, Create One!")
    return product

@router.put(
        "/<id:int>", 
        response_model=ShowProduct, 
        status_code=status.HTTP_202_ACCEPTED,
        dependencies=[Depends(require_permission(Permission.PRODUCT_UPDATE))]
        )
def update_product(id:int, data:UpdateProduct, by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    product_to_update = update_product_by_id(id=id, data=data, by_user=by_user, db=db)

    if product_to_update is None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Failed to update Product!")
    return product_to_update


@router.delete("/<id:int>", status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(require_permission(Permission.PRODUCT_DELETE))])
def delete_product(id:int, user:User=Depends(get_current_user), db:Session=Depends(get_db)):
    transaction = delete_product_by_id(id=id, db=db)
    if transaction:
        return Response({"Message":"Product Deleted!"}, status_code=status.HTTP_202_ACCEPTED)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Product Found, Create One!")