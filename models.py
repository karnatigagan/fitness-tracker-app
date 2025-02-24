from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime
import sqlite3

# Default to SQLite database
DATABASE_URL = 'sqlite:///fitness_tracker.db'

# Only try to use PostgreSQL if explicitly configured
if os.getenv('DATABASE_URL'):
    try:
        engine = create_engine(os.getenv('DATABASE_URL'))
        print("Using PostgreSQL database")
    except Exception as e:
        print(f"Failed to connect to PostgreSQL, using SQLite instead: {str(e)}")
        engine = create_engine(DATABASE_URL)
else:
    engine = create_engine(DATABASE_URL)
    print("Using SQLite database")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True)
    notifications_enabled = Column(Boolean, default=False)  # Default to False
    reminder_time = Column(String)  # Format: "HH:MM"

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, default=datetime.now().date())
    exercise = Column(String)
    duration = Column(Integer)  # in minutes
    intensity = Column(Integer)  # 1-10 scale
    user_id = Column(Integer, ForeignKey("users.id"))
    source = Column(String, default="manual")  # 'manual', 'apple_health'
    external_id = Column(String, nullable=True)  # ID from external source
    calories = Column(Float, nullable=True)
    distance = Column(Float, nullable=True)  # in meters
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    exercise = Column(String)
    target_duration = Column(Integer)  # minutes per week
    target_intensity = Column(Integer)  # 1-10 scale
    user_id = Column(Integer, ForeignKey("users.id"))

def init_db():
    """Initialize the database tables"""
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully")
    except Exception as e:
        print(f"Warning: Failed to create database tables: {str(e)}")

# Create all tables
init_db()

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()