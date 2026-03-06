from pydantic import BaseModel, ConfigDict
from datetime import date

class HabitCompletionRead(BaseModel):
    id: int
    completed_date: date

    model_config = ConfigDict(from_attributes=True)

class HabitCompletionStatsRead(BaseModel):
    habit_id: int
    total_completions: int 
    current_streak: int 
    longest_streak: int 