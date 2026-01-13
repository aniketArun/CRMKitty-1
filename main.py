from fastapi import FastAPI
from apis import base_router
from core.config import settings

app = FastAPI(
            title=settings.APP_NAME, 
            version=settings.APP_VERSION,
            description=settings.APP_DESCRIPTION
              )

app.include_router(prefix="/api", router=base_router.router)

