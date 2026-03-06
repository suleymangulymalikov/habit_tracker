from fastapi import FastAPI

from app.routers import habit, completion

app = FastAPI()

app.include_router(habit.router)
app.include_router(completion.router)
