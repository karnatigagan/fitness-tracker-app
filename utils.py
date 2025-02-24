import pandas as pd
from datetime import datetime
import os

def load_workout_data():
    """Load workout data from CSV file"""
    if not os.path.exists('workouts.csv'):
        return pd.DataFrame(columns=['date', 'exercise', 'duration', 'intensity'])
    return pd.read_csv('workouts.csv')

def save_workout(exercise, duration, intensity):
    """Save workout data to CSV file"""
    df = load_workout_data()
    new_workout = pd.DataFrame({
        'date': [datetime.now().strftime('%Y-%m-%d')],
        'exercise': [exercise],
        'duration': [duration],
        'intensity': [intensity]
    })
    df = pd.concat([df, new_workout], ignore_index=True)
    df.to_csv('workouts.csv', index=False)

def load_goals():
    """Load goals from CSV file"""
    if not os.path.exists('goals.csv'):
        return pd.DataFrame(columns=['exercise', 'target_duration', 'target_intensity'])
    return pd.read_csv('goals.csv')

def save_goal(exercise, target_duration, target_intensity):
    """Save goal to CSV file"""
    df = load_goals()
    new_goal = pd.DataFrame({
        'exercise': [exercise],
        'target_duration': [target_duration],
        'target_intensity': [target_intensity]
    })
    df = pd.concat([df, new_goal], ignore_index=True)
    df.to_csv('goals.csv', index=False)
