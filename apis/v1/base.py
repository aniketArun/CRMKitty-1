from fastapi import APIRouter
from apis.v1 import user_router, lead_router, customer_router, product_router


router = APIRouter()

router.include_router(prefix="/users",router=user_router.router, tags=["User"])
router.include_router(prefix="/leads",router=lead_router.router, tags=["Leads"])
router.include_router(prefix="/customer",router=customer_router.router, tags=["Customers"])
router.include_router(prefix="/product",router=product_router.router, tags=["Product"])



