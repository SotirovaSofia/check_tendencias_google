import os
import subprocess

# Define the path to the virtual environment
venv_path = os.path.join(os.getcwd(), 'venv')

# Create the virtual environment
subprocess.run(['python', '-m', 'venv', venv_path])

print(f"Virtual environment created at {venv_path}")


# Initialize a new git repository
subprocess.run(['git', 'init'])

# Add all files to the repository
subprocess.run(['git', 'add', '.'])

# Commit the files
subprocess.run(['git', 'commit', '-m', 'Initial commit'])

print("Git repository initialized and initial commit made.")


print("Vamos a hacer la primera modificación")