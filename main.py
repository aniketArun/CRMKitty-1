from fastapi import FastAPI
from apis import base_router
from core.config import settings
from fastapi.responses import RedirectResponse
from fastapi_pagination import add_pagination

app = FastAPI(
            title=settings.APP_NAME, 
            version=settings.APP_VERSION,
            description=settings.APP_DESCRIPTION
              )

@app.get("/")
def redirect_to_docs():
    # Redirects with a default status code of 307 (Temporary Redirect)
    return RedirectResponse(url="/docs")

app.include_router(prefix="/api", router=base_router.router)

add_pagination(app)