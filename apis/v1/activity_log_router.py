from fastapi import APIRouter, status, HTTPException, Depends
from fastapi_pagination import paginate, Page
from db.session import get_db
from sqlalchemy.orm import Session
from db.models.user import User
from schemas.activity_log import ActivityLog
from core.enums import Permission

from db.repository.activity_log import (
    get_logs_for_user, 
    get_logs_for_site,
    get_logs_for_lead,
    get_logs_for_product,
    get_logs_for_customer,
    get_logs_for_invoice,
    get_logs_for_report,
    get_logs_for_one_user,
    get_logs_for_profile
    )
from services.auth import (
    get_current_user, 
    require_permission
    )

router = APIRouter()


@router.get("/me", response_model=Page[ActivityLog], status_code=status.HTTP_200_OK)
def my_activity(by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    act = get_logs_for_user(user=by_user, db=db)
    if act is None:
        raise HTTPException(detail="No Activity", status_code=status.HTTP_404_NOT_FOUND)
    return paginate(act)

@router.get(
        "/admin", 
        response_model=Page[ActivityLog], 
        status_code=status.HTTP_200_OK,
        dependencies = [Depends(require_permission(Permission.SITE_ACTIVITY))]
        )
def admin_activity(by_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    act = get_logs_for_site(user=by_user, db=db)
    if act is None:
        raise HTTPException(detail="No Activity", status_code=status.HTTP_404_NOT_FOUND)
    return paginate(act)

@router.get(
        "/lead/{id}", 
        response_model=Page[ActivityLog], 
        status_code=status.HTTP_200_OK,
        dependencies = [Depends(require_permission(Permission.LEAD_READ))]
        )
def lead_activity(id:int, db:Session = Depends(get_db)):
    act = get_logs_for_lead(id=id, db=db)
    if act is None:
        raise HTTPException(detail="No Activity", status_code=status.HTTP_404_NOT_FOUND)
    return paginate(act)

@router.get(
        "/product/{id}", 
        response_model=Page[ActivityLog], 
        status_code=status.HTTP_200_OK,
        dependencies = [Depends(require_permission(Permission.PRODUCT_READ))]
        )
def product_activity(id:int, db:Session = Depends(get_db)):
    act = get_logs_for_product(id=id, db=db)
    if act is None:
        raise HTTPException(detail="No Activity", status_code=status.HTTP_404_NOT_FOUND)
    return paginate(act)

@router.get(
        "/report/{id}", 
        response_model=Page[ActivityLog], 
        status_code=status.HTTP_200_OK,
        dependencies = [Depends(require_permission(Permission.REPORT_READ))]
        )
def report_activity(id:int, db:Session = Depends(get_db)):
    act = get_logs_for_report(id=id, db=db)
    if act is None:
        raise HTTPException(detail="No Activity", status_code=status.HTTP_404_NOT_FOUND)
    return paginate(act)

@router.get(
        "/customer/{id}", 
        response_model=Page[ActivityLog], 
        status_code=status.HTTP_200_OK,
        dependencies = [Depends(require_permission(Permission.CUSTOMER_READ))]
        )
def cust_activity(id:int, db:Session = Depends(get_db)):
    act = get_logs_for_customer(id=id, db=db)
    if act is None:
        raise HTTPException(detail="No Activity", status_code=status.HTTP_404_NOT_FOUND)
    return paginate(act)

@router.get(
        "/invoice/{id}", 
        response_model=Page[ActivityLog], 
        status_code=status.HTTP_200_OK,
        dependencies = [Depends(require_permission(Permission.INVOICE_READ))]
        )
def invoice_activity(id:int, db:Session = Depends(get_db)):
    act = get_logs_for_invoice(id=id, db=db)
    if act is None:
        raise HTTPException(detail="No Activity", status_code=status.HTTP_404_NOT_FOUND)
    return paginate(act)

@router.get(
        "/user/{id}", 
        response_model=Page[ActivityLog], 
        status_code=status.HTTP_200_OK,
        dependencies = [Depends(require_permission(Permission.USER_READ))]
        )
def user_activity_all(id:int, db:Session = Depends(get_db)):
    act = get_logs_for_one_user(id, db=db)
    if act is None:
        raise HTTPException(detail="No Activity", status_code=status.HTTP_404_NOT_FOUND)
    return paginate(act)

@router.get(
        "/user-profile/{id}", 
        response_model=Page[ActivityLog], 
        status_code=status.HTTP_200_OK,
        dependencies = [Depends(require_permission(Permission.USER_READ))]
        )
def user_profile_activity(id:int, db:Session = Depends(get_db)):
    act = get_logs_for_profile(id, db=db)
    if act is None:
        raise HTTPException(detail="No Activity", status_code=status.HTTP_404_NOT_FOUND)
    return paginate(act)