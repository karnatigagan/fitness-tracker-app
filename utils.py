from datetime import datetime
from models import get_db, Workout, Goal
from sqlalchemy.orm import Session
from contextlib import contextmanager

@contextmanager
def get_db_context():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()

def load_workout_data():
    """Load workout data from database"""
    with get_db_context() as db:
        return db.query(Workout).all()

def save_workout(exercise, duration, intensity):
    """Save workout data to database"""
    with get_db_context() as db:
        new_workout = Workout(
            exercise=exercise,
            duration=duration,
            intensity=intensity,
            date=datetime.now().date()
        )
        db.add(new_workout)
        db.commit()

def load_goals():
    """Load goals from database"""
    with get_db_context() as db:
        return db.query(Goal).all()

def save_goal(exercise, target_duration, target_intensity):
    """Save goal to database"""
    with get_db_context() as db:
        new_goal = Goal(
            exercise=exercise,
            target_duration=target_duration,
            target_intensity=target_intensity
        )
        db.add(new_goal)
        db.commit()