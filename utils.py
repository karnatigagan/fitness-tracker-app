from datetime import datetime
from models import get_db, Workout, Goal, User
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
        # For now, use user_id=1 as default
        return db.query(Workout).filter(Workout.user_id == 1).all()

def save_workout(exercise, duration, intensity):
    """Save workout data to database"""
    with get_db_context() as db:
        new_workout = Workout(
            exercise=exercise,
            duration=duration,
            intensity=intensity,
            date=datetime.now().date(),
            user_id=1,  # Default user_id
            source='manual'
        )
        db.add(new_workout)
        db.commit()

def save_imported_workout(workout_data):
    """Save imported workout data to database"""
    try:
        with get_db_context() as db:
            # Check if workout already exists
            existing = db.query(Workout).filter(
                Workout.external_id == workout_data['external_id']
            ).first()

            if existing:
                return False  # Skip duplicates

            new_workout = Workout(
                exercise=workout_data['exercise'],
                duration=workout_data['duration'],
                intensity=7,  # Default intensity for imported workouts
                date=workout_data['start_time'].date(),
                start_time=workout_data['start_time'],
                end_time=workout_data['end_time'],
                calories=workout_data['calories'],
                distance=workout_data['distance'],
                source=workout_data['source'],
                external_id=workout_data['external_id'],
                user_id=1  # Default user_id
            )
            db.add(new_workout)
            db.commit()
            return True
    except Exception as e:
        print(f"Error saving imported workout: {str(e)}")
        return False

def load_goals():
    """Load goals from database"""
    with get_db_context() as db:
        # For now, use user_id=1 as default
        return db.query(Goal).filter(Goal.user_id == 1).all()

def save_goal(exercise, target_duration, target_intensity):
    """Save goal to database"""
    with get_db_context() as db:
        new_goal = Goal(
            exercise=exercise,
            target_duration=target_duration,
            target_intensity=target_intensity,
            user_id=1  # Default user_id
        )
        db.add(new_goal)
        db.commit()