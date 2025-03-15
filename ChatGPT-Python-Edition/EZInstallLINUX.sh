#!/bin/bash

# Set the path to your Python script
PYTHON_SCRIPT="%~dp0/Manual/installer.py"

# Ensure you are using the correct Python environment (optional)
# You can replace 'python3' with the specific Python interpreter if needed
python3 "$PYTHON_SCRIPT"

# Check if the script ran successfully
if [ $? -eq 0 ]; then
    echo "The 'openai' package installation check has been completed successfully."
else
    echo "An error occurred while checking or installing the 'openai' package."
fi
