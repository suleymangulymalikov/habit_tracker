from fastapi import FastAPI

from app.database.session import engine 
from app.database.base import Base 
from app.database import models 

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Habit Tracker API running"}
