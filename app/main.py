from fastapi import FastAPI

from app.database.session import engine 
from app.database.base import Base 
from app.database import models
from app.routers import habit, completion

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(habit.router)
app.include_router(completion.router)
