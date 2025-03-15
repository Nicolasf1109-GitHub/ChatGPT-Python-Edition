#!/bin/bash

# Set the path to the Python script
PYTHON_SCRIPT="%~dp0/run_openai_migrate.py"

# Ensure you are using the correct Python environment (optional)
# You can replace 'python3' with the specific Python interpreter if needed
python3 "$PYTHON_SCRIPT"

# Check if the script ran successfully
if [ $? -eq 0 ]; then
    echo "'openai migrate' has been successfully run."
else
    echo "An error occurred while running 'openai migrate'."
fi
