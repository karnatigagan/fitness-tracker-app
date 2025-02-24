import streamlit as st
from datetime import datetime
from models import User
from utils import get_db_context
from notifications import send_sms
import os

def check_twilio_config():
    """Check if Twilio is configured"""
    required_vars = ['TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN', 'TWILIO_PHONE_NUMBER']
    return all(os.getenv(var) for var in required_vars)

def render_notification_settings():
    """Render notification settings UI"""
    st.subheader("📱 Notification Settings")

    # Check if Twilio is configured
    twilio_configured = check_twilio_config()

    if not twilio_configured:
        st.info(
            "SMS notifications are currently disabled. They're optional and can be enabled later by setting up Twilio."
            "\n\nTo enable notifications:"
            "\n1. Create a free Twilio account at twilio.com"
            "\n2. Get your Account SID, Auth Token, and Phone Number"
            "\n3. Add them to your environment variables"
        )
        return

    with get_db_context() as db:
        # Get or create user (using a placeholder ID=1 for now)
        user = db.query(User).filter(User.id == 1).first()
        if not user:
            user = User(id=1)
            db.add(user)
            db.commit()

        with st.form("notification_settings"):
            phone_number = st.text_input(
                "Phone Number",
                value=user.phone_number if user.phone_number else "",
                help="Enter your phone number to receive notifications"
            )

            notifications_enabled = st.checkbox(
                "Enable Notifications",
                value=user.notifications_enabled,
                help="Receive workout reminders and goal updates"
            )

            reminder_time = st.time_input(
                "Daily Reminder Time",
                value=None if not user.reminder_time else datetime.strptime(user.reminder_time, "%H:%M").time(),
                help="When should we remind you to workout?"
            )

            save = st.form_submit_button("Save Settings")

            if save:
                user.phone_number = phone_number
                user.notifications_enabled = notifications_enabled
                user.reminder_time = reminder_time.strftime("%H:%M")
                db.commit()

                # Send test message if notifications are enabled
                if notifications_enabled and phone_number:
                    success = send_sms(
                        phone_number,
                        "🎉 Your fitness notifications are now set up! "
                        "You'll receive updates about your workouts and goals."
                    )
                    if success:
                        st.success("Settings saved! Test message sent to your phone.")
                    else:
                        st.error("Settings saved, but test message failed. Please check your phone number.")
                else:
                    st.success("Settings saved!")