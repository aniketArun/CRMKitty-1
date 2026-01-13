from fastapi import APIRouter, Depends, status, HTTPException
from schemas.product import CreateProduct, ShowProduct
from db.repository.product import create_new_product, get_all_products
from db.session import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

@router.post("/", response_model=ShowProduct, status_code=status.HTTP_201_CREATED)
def create_product(product:CreateProduct, db:Session = Depends(get_db)):
    new_product = create_new_product(product=product, db=db)

    if new_product is None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Failed to create new Product!")
    
    return new_product


@router.get("/", response_model=List[ShowProduct], status_code=status.HTTP_200_OK)
def all_products(db:Session = Depends(get_db)):
    products = get_all_products(db=db)

    if products is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Product have been created!")

    return products