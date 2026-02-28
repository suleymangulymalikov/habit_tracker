from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Annotated

from app.database.session import get_db 
from app.database.models import Habit
from app.schemas.habit import HabitCreate, HabitRead, HabitUpdate

router = APIRouter(
    prefix="/habits",
    tags = ["Habits"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=List[HabitRead])
# def get_all_habits(db: Session = Depends(get_db)):
def get_habits(db: db_dependency):
    habits = db.query(Habit).order_by(Habit.created_at, Habit.id).all()
    return habits

@router.get("/{habit_id}", response_model=HabitRead)
def get_habit(habit_id: int, db: db_dependency):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()

    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    return habit

@router.post("/", response_model=HabitRead)
def create_habit(habit: HabitCreate, db: db_dependency):
    new_habit = Habit(
        title = habit.title,
        description = habit.description
    )

    db.add(new_habit)
    db.commit()
    db.refresh(new_habit)

    return new_habit
    
@router.put("/{habit_id}", response_model=HabitRead)
def update_habit(habit_id: int, habit_update: HabitUpdate, db: db_dependency):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()

    if habit is None:
        raise HTTPException(status_code=404, detail="Habit Not Found")
    
    if habit_update.title is not None:
        habit.title = habit_update.title 
    
    if habit_update.description is not None:
        habit.description = habit_update.description 

    db.commit()
    db.refresh(habit)

    return habit

@router.delete("/{habit_id}", status_code=204)
def delete_habit(habit_id: int, db: db_dependency):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()

    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    db.delete(habit)
    db.commit()