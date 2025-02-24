import os
import subprocess
import webbrowser

def main():
    """
    Run the Fitness Tracker application.
    This script handles the startup configuration and launches the app.
    """
    # Set default Streamlit configuration
    os.environ['STREAMLIT_SERVER_PORT'] = '5000'
    os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'

    print("Starting Fitness Tracker App...")
    print("The app will be available at http://localhost:5000")
    
    try:
        # Run the Streamlit app
        subprocess.run(["streamlit", "run", "main.py"], check=True)
    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Error starting the app: {str(e)}")
        print("Please make sure Streamlit is installed: pip install streamlit")

if __name__ == "__main__":
    main()
