from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.models import Habit 

def get_habits(db: Session):
    return db.query(Habit).order_by(Habit.created_at, Habit.id).all()

def get_habit(habit_id: int, db: Session):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()

    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    return habit

def create_habit(habit, db):
    new_habit = Habit(
        title = habit.title,
        description = habit.description
    )

    db.add(new_habit)
    db.commit()
    db.refresh(new_habit)

    return new_habit

def update_habit(habit_id, habit_update, db):
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

def delete_habit(habit_id, db):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()

    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    db.delete(habit)
    db.commit()