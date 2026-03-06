from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated, List
from datetime import date

from app.database.session import get_db
from app.database.models import HabitCompletion, Habit
from app.schemas.completion import HabitCompletionRead

router = APIRouter(
    prefix="/habits",
    tags=["Completion"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/{habit_id}/completions", response_model=List[HabitCompletionRead])
def get_all_habit_completion(habit_id: int, db: db_dependency):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()

    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    habit_completions = db.query(HabitCompletion).filter(HabitCompletion.habit_id == habit.id)\
        .order_by(HabitCompletion.completed_date).all()
    
    return habit_completions

@router.post("/{habit_id}/complete", response_model=HabitCompletionRead)
def create_habit_completion(habit_id: int, db: db_dependency):
    today = date.today()
    habit = db.query(Habit).filter(Habit.id == habit_id).first()

    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    today_habit_completion = db.query(HabitCompletion)\
        .filter(HabitCompletion.habit_id == habit.id)\
        .filter(HabitCompletion.completed_date == today)\
            .first()
    
    if today_habit_completion:
        raise HTTPException(status_code=400, detail="Habit already completed today")
    
    new_habit_completion = HabitCompletion(
        habit_id = habit.id,
        completed_date = today
    )

    db.add(new_habit_completion)
    db.commit()
    db.refresh(new_habit_completion)

    return new_habit_completion
    