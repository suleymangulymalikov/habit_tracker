from fastapi import HTTPException
from datetime import date, timedelta 

from app.database.models import HabitCompletion, Habit 
from app.schemas.completion import HabitCompletionStatsRead

def get_all_habit_completions(habit_id, db):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()

    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    habit_completions = db.query(HabitCompletion).filter(HabitCompletion.habit_id == habit.id)\
        .order_by(HabitCompletion.completed_date).all()
    
    return habit_completions

def create_habit_completion(habit_id, db):
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

def get_habit_stats(habit_id, db):
    habit = db.query(Habit).filter(Habit.id == habit_id).first() 
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    completions = db.query(HabitCompletion).filter(HabitCompletion.habit_id == habit.id)\
        .order_by(HabitCompletion.completed_date).all()
    
    dates = [c.completed_date for c in completions]
    
    total_completions = len(dates)

    if not dates:
        return HabitCompletionStatsRead(
            habit_id = habit.id,
            total_completions = total_completions,
            longest_streak = 0,
            current_streak = 0
        )
    
    longest_streak = 0
    current_streak = 1

    for i in range(1, len(dates)):
        diff = (dates[i] - dates[i - 1]).days 

        if diff == 1:
            current_streak += 1
        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1
    
    longest_streak = max(longest_streak, current_streak)

    last_date = dates[-1]
    today = date.today()

    if last_date not in (today, today - timedelta(days=1)):
        current_streak = 0

    return HabitCompletionStatsRead(
            habit_id = habit.id,
            total_completions = total_completions,
            longest_streak = longest_streak,
            current_streak = current_streak
            )
 