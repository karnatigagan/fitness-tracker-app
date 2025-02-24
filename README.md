# 📱 Fitness Tracker App

A mobile-optimized web application for tracking your fitness journey, built with Streamlit and Python.

## Features

- 🏃‍♂️ Quick and easy workout logging
- 📊 Progress visualization with interactive charts
- 🎯 Goal setting and progress tracking
- 📱 Mobile-friendly interface

## Tech Stack

- Python 3.11
- Streamlit for web interface
- PostgreSQL for data storage
- SQLAlchemy ORM
- Plotly for data visualization
- Pandas for data processing

## Project Structure

```
├── components/           # UI components
│   ├── workout_form.py  # Workout logging form
│   ├── progress_charts.py # Progress visualization
│   └── goals.py         # Goals management
├── models.py            # Database models
├── utils.py            # Utility functions
├── main.py             # Main application
└── styles.css          # Custom styles
```

## Setup

1. Install dependencies:
```bash
pip install streamlit pandas plotly sqlalchemy psycopg2-binary python-dotenv
```

2. Set up environment variables:
- Create a `.env` file with your PostgreSQL database URL:
```
DATABASE_URL=postgresql://user:password@host:port/dbname
```

3. Run the application:
```bash
streamlit run main.py
```

## Usage

1. **Log Workouts**: Use the "Log Workout" tab to record your exercises
2. **Track Progress**: View your progress charts in the "Progress" tab
3. **Set Goals**: Create and monitor fitness goals in the "Goals" tab

## Contributing

Feel free to open issues or submit pull requests to help improve the application.

## License

MIT License
