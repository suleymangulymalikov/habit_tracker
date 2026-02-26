from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

from app.database.base import Base 

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True) 
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)