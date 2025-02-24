import os
from twilio.rest import Client
from datetime import datetime, timedelta
from models import User, Workout, Goal
from utils import get_db_context

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

def send_sms(phone_number: str, message: str) -> bool:
    """Send SMS using Twilio"""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        return True
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")
        return False

def send_workout_reminder(user_id: int) -> None:
    """Send workout reminder to user"""
    with get_db_context() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if user and user.notifications_enabled:
            message = (
                "🏃‍♂️ Time for your workout! "
                "Stay consistent and achieve your fitness goals. "
                "Log your progress in the Fitness Tracker app!"
            )
            send_sms(user.phone_number, message)

def send_goal_achievement_notification(user_id: int, exercise: str) -> None:
    """Send notification when user reaches a goal"""
    with get_db_context() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if user and user.notifications_enabled:
            message = (
                f"🎉 Congratulations! You've reached your {exercise} goal! "
                "Keep up the great work! 💪"
            )
            send_sms(user.phone_number, message)

def send_weekly_summary(user_id: int) -> None:
    """Send weekly workout summary"""
    with get_db_context() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if not user or not user.notifications_enabled:
            return

        # Get last week's workouts
        week_ago = datetime.now().date() - timedelta(days=7)
        workouts = db.query(Workout).filter(
            Workout.user_id == user_id,
            Workout.date > week_ago
        ).all()

        if not workouts:
            message = (
                "📊 Weekly Summary:\n"
                "No workouts logged this week. "
                "Let's get active! 💪"
            )
        else:
            total_duration = sum(w.duration for w in workouts)
            avg_intensity = sum(w.intensity for w in workouts) / len(workouts)
            message = (
                "📊 Weekly Summary:\n"
                f"- {len(workouts)} workouts completed\n"
                f"- {total_duration} total minutes\n"
                f"- {avg_intensity:.1f}/10 avg intensity\n"
                "Keep pushing! 💪"
            )

        send_sms(user.phone_number, message)
