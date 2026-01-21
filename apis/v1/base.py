from fastapi import APIRouter
from apis.v1 import (
    user_router, 
    lead_router, 
    customer_router, 
    product_router, 
    invoice_router, 
    report_router, 
    role_router, 
    login_router, 
    company_router,
    follow_up_router,
    activity_log_router
    )


router = APIRouter()

router.include_router(prefix="/users",router=user_router.router, tags=["User"])
router.include_router(prefix="/auth",router=login_router.router, tags=["Auth"])
router.include_router(prefix="/role",router=role_router.router, tags=["Role"])
router.include_router(prefix="/activity-log",router=activity_log_router.router, tags=["ActivityLog"])
router.include_router(prefix="/company",router=company_router.router, tags=["Company"])
router.include_router(prefix="/leads",router=lead_router.router, tags=["Leads"])
router.include_router(prefix="/customer",router=customer_router.router, tags=["Customers"])
router.include_router(prefix="/product",router=product_router.router, tags=["Product"])
router.include_router(prefix="/invoice",router=invoice_router.router, tags=["Invoice"])
router.include_router(prefix="/report",router=report_router.router, tags=["Report"])
router.include_router(prefix="/follow-up",router=follow_up_router.router, tags=["FollowUp"])







