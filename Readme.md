# WhatsApp Message Automation Script

## Function
This script automates sending messages in the WhatsApp application. It allows the user to specify a message and the number of times it should be sent. The script utilizes the `pyautogui` library to interact with the WhatsApp chat window.

## How It Works
1. The script accepts two command-line arguments:
   - `limit`: Number of times the message should be sent.
   - `message`: The text message to be sent.
2. After execution, the script waits 5 seconds to allow the user to switch to the WhatsApp chat window.
3. It then types and sends the message the specified number of times.
4. A success message is displayed when the process is complete.

## How to Use
### Prerequisites
- Install Python
- Install `pyautogui` using:
  ```sh
  pip install pyautogui
  ```

### Running the Script
1. Open a terminal or command prompt.
2. Run the script with the required parameters:
   ```sh
   python SpamChat.py <limit> "<message>"
   ```
   Example:
   ```sh
   python SpamChat.py 5 "Hello, this is an automated message!"
   ```
<img src="https://github.com/user-attachments/assets/ba4af2e8-80b3-4edc-a5f3-b01eb579393d" width="500" height="auto">

3. Switch to the WhatsApp chat window within 5 seconds.
4. The script will start sending messages automatically.
<img src="https://github.com/user-attachments/assets/f4fb8d75-c1a3-4fcd-925d-426c2a82fcbc" width="500" height="auto">


## Notes
- Ensure WhatsApp Web or the WhatsApp application is open and active.
- Use responsibly; excessive spamming may violate WhatsApp policies.
- The script requires focus on the chat window; avoid using other applications while running it.

