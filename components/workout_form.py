import streamlit as st
from utils import save_workout

def render_workout_form():
    """Render the workout logging form"""
    st.subheader("Log Your Workout")
    
    with st.form("workout_form"):
        exercise = st.selectbox(
            "Exercise Type",
            ["Running", "Cycling", "Swimming", "Weight Training", "Yoga", "Other"]
        )
        
        duration = st.number_input(
            "Duration (minutes)",
            min_value=1,
            max_value=300,
            value=30
        )
        
        intensity = st.slider(
            "Intensity Level",
            min_value=1,
            max_value=10,
            value=5,
            help="1 = Very Light, 10 = Maximum Effort"
        )
        
        submit = st.form_submit_button("Save Workout")
        
        if submit:
            save_workout(exercise, duration, intensity)
            st.success("Workout logged successfully!")
            return True
    return False
