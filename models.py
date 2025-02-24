from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise EnvironmentError(
        "DATABASE_URL not found. Please create a .env file with your database configuration."
    )

try:
    # Create database engine
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    raise Exception(f"Failed to connect to database: {str(e)}")

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True)
    notifications_enabled = Column(Boolean, default=True)
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
        raise Exception(f"Failed to create database tables: {str(e)}")

# Create all tables
init_db()

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()