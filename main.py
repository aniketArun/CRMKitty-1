from fastapi import FastAPI
from apis.v1 import base

app = FastAPI()

app.include_router(prefix="/v1", router=base.router)

