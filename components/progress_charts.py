import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils import load_workout_data
import pandas as pd
from datetime import datetime, timedelta

def render_progress_charts():
    """Render progress visualization charts"""
    st.subheader("Your Progress")

    workouts = load_workout_data()
    if not workouts:
        st.info("No workout data available. Start logging your workouts!")
        return

    # Convert workout objects to DataFrame
    df = pd.DataFrame([
        {
            'date': w.date,
            'exercise': w.exercise,
            'duration': w.duration,
            'intensity': w.intensity
        } for w in workouts
    ])

    # Weekly summary
    weekly_stats = df.groupby(pd.Grouper(key='date', freq='W'))['duration'].sum().reset_index()

    # Duration trend
    fig_duration = px.line(
        weekly_stats,
        x='date',
        y='duration',
        title='Weekly Workout Duration',
        labels={'duration': 'Total Minutes', 'date': 'Week'}
    )
    st.plotly_chart(fig_duration, use_container_width=True)

    # Exercise distribution
    exercise_dist = df['exercise'].value_counts()
    fig_dist = px.pie(
        values=exercise_dist.values,
        names=exercise_dist.index,
        title='Exercise Distribution'
    )
    st.plotly_chart(fig_dist, use_container_width=True)

    # Recent statistics
    st.subheader("Recent Statistics")
    col1, col2, col3 = st.columns(3)

    with col1:
        total_workouts = len(df)
        recent_workouts = len(df[df['date'] > datetime.now().date() - timedelta(days=7)])
        st.metric(
            "Total Workouts",
            total_workouts,
            delta=recent_workouts
        )

    with col2:
        avg_duration = df['duration'].mean()
        recent_avg = df['duration'].tail(5).mean()
        st.metric(
            "Avg Duration",
            f"{avg_duration:.0f} min",
            delta=f"{recent_avg - avg_duration:.0f} min"
        )

    with col3:
        avg_intensity = df['intensity'].mean()
        recent_intensity = df['intensity'].tail(5).mean()
        st.metric(
            "Avg Intensity",
            f"{avg_intensity:.1f}/10",
            delta=f"{recent_intensity - avg_intensity:.1f}"
        )