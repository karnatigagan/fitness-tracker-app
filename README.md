# 📱 Fitness Tracker App

A mobile-optimized web application for tracking your fitness journey, built with Streamlit and Python.

## Features

- 🏃‍♂️ Quick and easy workout logging
- 📊 Progress visualization with interactive charts
- 🎯 Goal setting and progress tracking
- 📱 Mobile-friendly interface
- 🔄 Apple Health data import
- 📲 Optional SMS notifications for workout reminders

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/karnatigagan/fitness-tracker-app.git
cd fitness-tracker-app
```

2. Install required packages:
```bash
pip install streamlit pandas plotly sqlalchemy
```

3. Run the app:
```bash
python run.py
```

The app will start automatically and be accessible at `http://localhost:5000`

## Optional Features

### SMS Notifications
To enable SMS notifications, install additional dependencies and set up Twilio:

1. Install Twilio:
```bash
pip install twilio python-dotenv
```

2. Create a free account at [twilio.com](https://www.twilio.com)
3. Create a `.env` file with your Twilio credentials:
```
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_phone
```

### PostgreSQL Database
By default, the app uses SQLite. To use PostgreSQL:

1. Install PostgreSQL dependencies:
```bash
pip install psycopg2-binary
```

2. Add your database URL to `.env`:
```
DATABASE_URL=postgresql://user:password@host:port/dbname
```

## Usage

1. **Log Workouts**: Use the "Log Workout" tab to record your exercises
2. **Track Progress**: View your progress charts in the "Progress" tab
3. **Set Goals**: Create and monitor fitness goals in the "Goals" tab
4. **Import Health Data**: Import your workouts from Apple Health
5. **Enable Notifications**: Set up optional SMS reminders in the Goals tab

## Contributing

Feel free to open issues or submit pull requests to help improve the application.

## License

MIT License