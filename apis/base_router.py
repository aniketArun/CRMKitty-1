from apis.v1 import base
from fastapi import APIRouter

router = APIRouter()

router.include_router(prefix="/v1", router=base.router)