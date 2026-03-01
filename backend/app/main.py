from fastapi import FastAPI
from app.api.health import router as health_router
from app.db.session import engine
from app.db.base import Base
from app.models import user
from app.api.auth import router as auth_router

app = FastAPI(title="SecureSight API")

Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(auth_router)