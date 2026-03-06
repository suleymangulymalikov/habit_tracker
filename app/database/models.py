from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Date, UniqueConstraint
from datetime import datetime, timezone, date
from typing import List

from app.database.base import Base 

class Habit(Base):
    __tablename__ = "habits"

    id: Mapped[int] = mapped_column(Integer, primary_key=True) 
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc), nullable=False)

    completions: Mapped[List["HabitCompletion"]] = relationship(
        "HabitCompletion",
        back_populates="habit",
        cascade="all, delete-orphan"
    )

class HabitCompletion(Base):
    __tablename__ = "habit_completions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    habit_id: Mapped[int] = mapped_column(Integer, ForeignKey("habits.id", ondelete="CASCADE"), nullable=False)
    completed_date: Mapped[date] = mapped_column(Date, default=date.today, nullable=False)

    __table_args__ = (
        UniqueConstraint("habit_id", "completed_date", name="uq_habit_completion_per_day"),
    )

    habit: Mapped["Habit"] = relationship("Habit", back_populates="completions")