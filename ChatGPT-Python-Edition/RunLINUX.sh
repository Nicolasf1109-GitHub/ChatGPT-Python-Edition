#!/bin/bash

# Set the path to your Python script
PYTHON_SCRIPT="%~dp0/Manual/main.py"

# Ensure you are using the correct Python environment (optional)
# You can replace 'python3' with the specific Python interpreter if needed
python3 "$PYTHON_SCRIPT"

# Check if the script ran successfully
if [ $? -eq 0 ]; then
    echo "ChatGPT CLI session has ended successfully."
else
    echo "An error occurred while running the ChatGPT CLI script."
fi
