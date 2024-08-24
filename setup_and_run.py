import os
import subprocess
import sys

# Define the environment name
env_name = "venv"

# Step 1: Create a virtual environment
print("Creating virtual environment...")
subprocess.check_call([sys.executable, "-m", "venv", env_name])

# Step 2: Activate the virtual environment
# Detect the platform to use the correct activation command
if os.name == 'nt':  # Windows
    activate_script = os.path.join(env_name, 'Scripts', 'activate.bat')
else:  # macOS/Linux
    activate_script = os.path.join(env_name, 'bin', 'activate')

# Activate the virtual environment
activate_command = f"{activate_script}"
print(f"Activating virtual environment: {activate_command}")
subprocess.call(activate_command, shell=True)

# Step 3: Install necessary dependencies
print("Installing dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit", "pandas", "plotly", "pandasql"])

# Step 4: Run the Streamlit application
print("Running the Streamlit application...")
subprocess.check_call([sys.executable, "-m", "streamlit", "run", "app.py"])
