from fastapi import FastAPI
from sqlmodel import SQLModel

from database import engine
from core.config import settings

from model.producto import Producto


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {
        "status": "success",
        "code": 200,
        "message": "Hello World"
        }
