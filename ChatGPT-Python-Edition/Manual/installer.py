import subprocess
import sys

def install_openai():
    try:
        # Check if the openai package is installed
        import openai
        print("The 'openai' package is already installed.")
    except ImportError:
        print("The 'openai' package is not installed. Installing...")
        # Install openai package using pip
        subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
        print("The 'openai' package has been installed successfully.")

if __name__ == "__main__":
    install_openai()
