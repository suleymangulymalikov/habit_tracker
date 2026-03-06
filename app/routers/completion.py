from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated, List

from app.database.session import get_db
from app.schemas.completion import HabitCompletionRead, HabitCompletionStatsRead
from app.services import completion_service

router = APIRouter(
    prefix="/habits",
    tags=["Completion"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/{habit_id}/completions", response_model=List[HabitCompletionRead])
def get_all_habit_completion(habit_id: int, db: db_dependency):
    return completion_service.get_all_habit_completions(habit_id, db)

@router.post("/{habit_id}/complete", response_model=HabitCompletionRead)
def create_habit_completion(habit_id: int, db: db_dependency):
    return completion_service.create_habit_completion(habit_id, db)
    
@router.get("/{habit_id}/stats", response_model=HabitCompletionStatsRead)
def get_habit_stats(habit_id: int, db: db_dependency):
    return completion_service.get_habit_stats(habit_id, db)    

        
