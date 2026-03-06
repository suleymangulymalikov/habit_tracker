from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Annotated

from app.database.session import get_db 
from app.schemas.habit import HabitCreate, HabitRead, HabitUpdate
from app.services import habit_service

router = APIRouter(
    prefix="/habits",
    tags = ["Habits"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=List[HabitRead])
def get_habits(db: db_dependency):
    return habit_service.get_habits(db)

@router.get("/{habit_id}", response_model=HabitRead)
def get_habit(habit_id: int, db: db_dependency):
    return habit_service.get_habit(habit_id, db)

@router.post("/", response_model=HabitRead)
def create_habit(habit: HabitCreate, db: db_dependency):
    return habit_service.create_habit(habit, db)
    
@router.put("/{habit_id}", response_model=HabitRead)
def update_habit(habit_id: int, habit_update: HabitUpdate, db: db_dependency):
    return habit_service.update_habit(habit_id, habit_update, db)

@router.delete("/{habit_id}", status_code=204)
def delete_habit(habit_id: int, db: db_dependency):
    return habit_service.delete_habit(habit_id, db)