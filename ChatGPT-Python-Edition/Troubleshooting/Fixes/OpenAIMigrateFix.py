import subprocess
import sys

def run_openai_migrate():
    try:
        # Run the openai migrate command
        print("Running 'openai migrate' to complete setup...")
        subprocess.check_call([sys.executable, "-m", "openai", "migrate"])
        print("'openai migrate' has been successfully run.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running 'openai migrate': {e}")
    except FileNotFoundError:
        print("The 'openai' command was not found. Please ensure the OpenAI CLI is installed.")

if __name__ == "__main__":
    run_openai_migrate()
