import streamlit as st
from utils import save_goal, load_goals, load_workout_data
import pandas as pd
from datetime import datetime, timedelta

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
    goals = load_goals()
    workouts = load_workout_data()

    if goals:
        st.subheader("Current Goals")

        # Convert workouts to DataFrame for easier processing
        if workouts:
            workouts_df = pd.DataFrame([
                {
                    'date': w.date,
                    'exercise': w.exercise,
                    'duration': w.duration
                } for w in workouts
            ])
            recent_date = datetime.now().date() - timedelta(days=7)
            recent_workouts = workouts_df[workouts_df['date'] > recent_date]

        for goal in goals:
            with st.container():
                st.write(f"**{goal.exercise}**")

                # Calculate progress
                if workouts and not recent_workouts.empty:
                    weekly_duration = recent_workouts[
                        recent_workouts['exercise'] == goal.exercise
                    ]['duration'].sum()

                    progress = (weekly_duration / goal.target_duration) * 100
                    progress = min(progress, 100)

                    st.progress(progress / 100)
                    st.write(f"Weekly progress: {weekly_duration:.0f}/{goal.target_duration:.0f} minutes")
                else:
                    st.progress(0)
                    st.write("No recent workouts logged")