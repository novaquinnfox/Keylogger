# Python Keylogger (For Educational Use Only)

This is a simple Python-based **keylogger** built using the `keyboard` module. It records keystrokes until the `Enter` key is pressed and logs them to a file with a timestamp. This tool is intended **strictly for ethical, educational, or cybersecurity research purposes**.

---

## Features

-  Global keyboard listener
-  Captures input until `Enter` is pressed
-  Logs keystrokes with timestamps
-  Saves logs to `keylog_data.txt`
-  Press `Esc` to safely exit
-  Lightweight and beginner-friendly code

---

## Disclaimer

>**This tool is intended for educational and research purposes only.**
>
> Unauthorized use of keyloggers is **illegal** and **unethical**.  
> Do **not** use this script on any device you do not own or have explicit permission to analyze.

---

## Requirements

- Python 3.6+
- Windows OS (run with admin privileges)
- Python module:
  ```bash
  pip install keyboard

## How To Run:

1. Clone this repository
  >`git clone https://github.com/novaquinnfox/Keylogger.git`
>
  >`cd python-keylogger`
2. Install dependencies
  >  `pip install keyboard`
3. Run the script as Administrator
  >  `python keylogger.py`
4. Switch to another window (like Notepad or a browser)
 -  Type something
 -  Press Enter
 -  The text will be saved in keylog_data.txt
5. Press `Esc` to stop the keylogger and safely exit.
