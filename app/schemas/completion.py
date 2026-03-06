from pydantic import BaseModel, ConfigDict
from datetime import date

class HabitCompletionRead(BaseModel):
    id: int
    completed_date: date

    model_config = ConfigDict(from_attributes=True)