import streamlit as st
from components.workout_form import render_workout_form
from components.progress_charts import render_progress_charts
from components.goals import render_goals
from components.health_import import render_health_import

# Page configuration
st.set_page_config(
    page_title="Fitness Tracker",
    page_icon="💪",
    layout="wide"
)

# Load custom CSS
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# App title
st.title("📱 Fitness Tracker")

# Navigation
tab1, tab2, tab3, tab4 = st.tabs([
    "Log Workout",
    "Progress",
    "Goals",
    "Import Health Data"
])

with tab1:
    render_workout_form()

with tab2:
    render_progress_charts()

with tab3:
    render_goals()

with tab4:
    render_health_import()

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Stay fit, stay healthy! 💪</p>
    </div>
    """,
    unsafe_allow_html=True
)