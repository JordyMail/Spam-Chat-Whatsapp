import sys
import pyautogui as pt
import time

try:
    limit = sys.argv[1]  # First command-line argument
    message = sys.argv[2]  # Second command-line argument

    if not limit.isdigit():
        raise ValueError("Please enter a valid number for the limit.")

    limit = int(limit)  # Convert to integer
    i = 0

    print("Switch to WhatsApp chat window. Automation will start in 5 seconds...")
    time.sleep(5)
  
    while i < limit:
        pt.typewrite(message)
        pt.press("enter")
        i += 1  

    print(f"Successfully sent {limit} messages.")
except IndexError:
    print("Usage: python SpamChat.py <limit> <message>")
except ValueError as e:
    print(f"Error: {e}")
