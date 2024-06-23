import hypercorn
from fastapi import FastAPI
from app.router.router import router
from app.db.config import settings
from app.db.base import db

def init_app():
    app = FastAPI()

    app.include_router(router)
    return app

app = init_app()

#app.include_router(router, prefix="/api")