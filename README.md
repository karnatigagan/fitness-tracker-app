# 📱 Fitness Tracker App

A mobile-optimized web application for tracking your fitness journey, built with Streamlit and Python.

## Features

- 🏃‍♂️ Quick and easy workout logging
- 📊 Progress visualization with interactive charts
- 🎯 Goal setting and progress tracking
- 📱 Mobile-friendly interface
- 🔄 Apple Health data import
- 📲 SMS notifications for workout reminders

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/karnatigagan/fitness-tracker-app.git
cd fitness-tracker-app
```

2. Install required packages:
```bash
pip install streamlit pandas plotly sqlalchemy psycopg2-binary python-dotenv twilio
```

3. Set up environment variables:
Create a `.env` file in the project root with:
```
DATABASE_URL=postgresql://user:password@host:port/dbname
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_phone
```

4. Run the app:
```bash
streamlit run main.py
```

The app will open in your default browser at `http://localhost:8501`

## Project Structure

```
├── components/           # UI components
│   ├── workout_form.py  # Workout logging form
│   ├── progress_charts.py # Progress visualization
│   ├── goals.py         # Goals management
│   ├── health_import.py # Apple Health import
│   └── notification_settings.py # SMS notifications
├── models.py            # Database models
├── utils.py            # Utility functions
├── main.py             # Main application
└── styles.css          # Custom styles
```

## Usage

1. **Log Workouts**: Use the "Log Workout" tab to record your exercises
2. **Track Progress**: View your progress charts in the "Progress" tab
3. **Set Goals**: Create and monitor fitness goals in the "Goals" tab
4. **Import Health Data**: Import your workouts from Apple Health
5. **Enable Notifications**: Set up SMS reminders in the Goals tab

## Contributing

Feel free to open issues or submit pull requests to help improve the application.

## License

MIT License