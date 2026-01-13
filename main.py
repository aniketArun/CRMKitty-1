from fastapi import FastAPI
from apis.v1 import base
from core.config import settings

app = FastAPI(
            title=settings.APP_NAME, 
            version=settings.APP_VERSION,
            description=settings.APP_DESCRIPTION
              )

app.include_router(prefix="/v1", router=base.router)

