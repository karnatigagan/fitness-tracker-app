import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils import load_workout_data
import pandas as pd

def render_progress_charts():
    """Render progress visualization charts"""
    st.subheader("Your Progress")
    
    df = load_workout_data()
    if df.empty:
        st.info("No workout data available. Start logging your workouts!")
        return
    
    # Prepare data
    df['date'] = pd.to_datetime(df['date'])
    
    # Weekly summary
    weekly_stats = df.groupby([pd.Grouper(key='date', freq='W')])['duration'].sum().reset_index()
    
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
        st.metric(
            "Total Workouts",
            len(df),
            delta=len(df[df['date'] > pd.Timestamp.now() - pd.Timedelta(days=7)])
        )
    
    with col2:
        avg_duration = df['duration'].mean()
        st.metric(
            "Avg Duration",
            f"{avg_duration:.0f} min",
            delta=f"{df['duration'].tail(5).mean() - avg_duration:.0f} min"
        )
    
    with col3:
        avg_intensity = df['intensity'].mean()
        st.metric(
            "Avg Intensity",
            f"{avg_intensity:.1f}/10",
            delta=f"{df['intensity'].tail(5).mean() - avg_intensity:.1f}"
        )
