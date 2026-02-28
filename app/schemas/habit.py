from pydantic import BaseModel
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

    class Config:
        from_attributes = True 

class HabitUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None