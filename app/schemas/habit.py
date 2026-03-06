from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class HabitBase(BaseModel):
    title: str
    description: Optional[str] = None 

class HabitCreate(HabitBase):
    pass 

class HabitRead(HabitBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HabitUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None