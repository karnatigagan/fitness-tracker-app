import streamlit as st
from utils import save_goal, load_goals, load_workout_data
import pandas as pd

def render_goals():
    """Render the goals section"""
    st.subheader("Fitness Goals")
    
    # Goal setting form
    with st.form("goal_form"):
        exercise = st.selectbox(
            "Exercise Type",
            ["Running", "Cycling", "Swimming", "Weight Training", "Yoga", "Other"]
        )
        
        target_duration = st.number_input(
            "Target Duration (minutes/week)",
            min_value=30,
            max_value=1000,
            value=150
        )
        
        target_intensity = st.number_input(
            "Target Intensity",
            min_value=1,
            max_value=10,
            value=7
        )
        
        submit = st.form_submit_button("Set Goal")
        
        if submit:
            save_goal(exercise, target_duration, target_intensity)
            st.success("Goal set successfully!")
    
    # Display current goals and progress
    goals_df = load_goals()
    workouts_df = load_workout_data()
    
    if not goals_df.empty:
        st.subheader("Current Goals")
        
        for _, goal in goals_df.iterrows():
            with st.container():
                st.write(f"**{goal['exercise']}**")
                
                # Calculate progress
                if not workouts_df.empty:
                    weekly_duration = workouts_df[
                        (workouts_df['exercise'] == goal['exercise']) &
                        (pd.to_datetime(workouts_df['date']) > pd.Timestamp.now() - pd.Timedelta(days=7))
                    ]['duration'].sum()
                    
                    progress = (weekly_duration / goal['target_duration']) * 100
                    progress = min(progress, 100)
                    
                    st.progress(progress / 100)
                    st.write(f"Weekly progress: {weekly_duration:.0f}/{goal['target_duration']:.0f} minutes")
