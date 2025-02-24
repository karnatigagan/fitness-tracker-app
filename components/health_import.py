import streamlit as st
import pandas as pd
from datetime import datetime
from utils import save_imported_workout
import xml.etree.ElementTree as ET
import io

def parse_apple_health_export(file):
    """Parse Apple Health Export XML file"""
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        
        workouts = []
        for workout in root.findall('.//Workout'):
            workout_data = {
                'type': workout.get('workoutActivityType'),
                'duration': float(workout.get('duration', 0)) / 60,  # Convert to minutes
                'start_time': datetime.fromisoformat(workout.get('startDate', '')),
                'end_time': datetime.fromisoformat(workout.get('endDate', '')),
                'calories': float(workout.get('totalEnergyBurned', 0)),
                'distance': float(workout.get('totalDistance', 0)),
                'source': 'apple_health',
                'external_id': workout.get('uuid', '')
            }
            
            # Map Apple Health workout types to our exercise types
            workout_data['exercise'] = map_workout_type(workout_data['type'])
            workouts.append(workout_data)
            
        return workouts
    except Exception as e:
        st.error(f"Error parsing file: {str(e)}")
        return None

def map_workout_type(apple_type):
    """Map Apple Health workout types to our exercise types"""
    mapping = {
        'HKWorkoutActivityTypeRunning': 'Running',
        'HKWorkoutActivityTypeCycling': 'Cycling',
        'HKWorkoutActivityTypeSwimming': 'Swimming',
        'HKWorkoutActivityTypeTraditionalStrengthTraining': 'Weight Training',
        'HKWorkoutActivityTypeYoga': 'Yoga'
    }
    return mapping.get(apple_type, 'Other')

def render_health_import():
    """Render health data import interface"""
    st.subheader("📱 Import Health Data")
    
    uploaded_file = st.file_uploader(
        "Upload Apple Health Export (XML)",
        type=['xml'],
        help="Export your health data from the Apple Health app and upload the XML file"
    )
    
    if uploaded_file:
        workouts = parse_apple_health_export(uploaded_file)
        
        if workouts:
            st.success(f"Found {len(workouts)} workouts in the file")
            
            # Display preview
            st.subheader("Preview of Found Workouts")
            preview_df = pd.DataFrame(workouts)
            st.dataframe(
                preview_df[[
                    'exercise', 'duration', 'start_time',
                    'calories', 'distance'
                ]]
            )
            
            if st.button("Import Workouts"):
                imported = 0
                for workout in workouts:
                    if save_imported_workout(workout):
                        imported += 1
                
                st.success(f"Successfully imported {imported} workouts!")
                
                # Show instructions for viewing imported data
                st.info(
                    "Your imported workouts will appear in the Progress tab. "
                    "They'll be included in your statistics and goal tracking."
                )
