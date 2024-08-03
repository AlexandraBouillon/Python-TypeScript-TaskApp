python
from fastapi import FastAPI
from app.routes import task_routes
from app.utils.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(task_routes.router, prefix="/tasks", tags=["tasks"])