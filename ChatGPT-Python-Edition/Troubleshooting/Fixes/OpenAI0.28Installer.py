import subprocess
import sys

def install_openai():
    try:
        # Run the pip install command for openai version 0.28
        subprocess.check_call([sys.executable, "-m", "pip", "install", "openai==0.28"])
        print("OpenAI package (version 0.28) installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing OpenAI package: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_openai()
