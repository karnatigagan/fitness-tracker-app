from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime
import sqlite3

print("Initializing database configuration...")

# Default to SQLite database
DATABASE_URL = 'sqlite:///fitness_tracker.db'
print(f"Using database URL: {DATABASE_URL}")

# Create database engine
try:
    engine = create_engine(DATABASE_URL)
    print("Successfully created database engine")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    print(f"Error creating database engine: {str(e)}")
    raise

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, nullable=True)
    notifications_enabled = Column(Boolean, default=False)
    reminder_time = Column(String, nullable=True)

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, default=datetime.now().date())
    exercise = Column(String)
    duration = Column(Integer)  # in minutes
    intensity = Column(Integer)  # 1-10 scale
    user_id = Column(Integer, ForeignKey("users.id"))
    source = Column(String, default="manual")
    external_id = Column(String, nullable=True)
    calories = Column(Float, nullable=True)
    distance = Column(Float, nullable=True)
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
        print("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully")
    except Exception as e:
        print(f"Error creating database tables: {str(e)}")
        raise

# Create all tables
init_db()

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()