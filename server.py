from flask import Flask, request, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'screenshots'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_screenshot():
    file = request.files['file']
    if file:
        # Create a unique filename with a timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        filename = f"screenshot_{timestamp}.png"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        print(f"Saved new screenshot: {file_path}")
        return "Screenshot uploaded successfully", 200
    return "No file part in the request", 400

@app.route('/')
def index():
    # This will display the latest uploaded screenshot
    try:
        # Get a list of all files in the directory
        files = os.listdir(UPLOAD_FOLDER)
        # Sort them by name (which includes timestamp)
        files.sort()
        # Get the last one
        latest_file = files[-1]
        return send_from_directory(UPLOAD_FOLDER, latest_file)
    except Exception as e:
        return "No screenshots uploaded yet.", 404

if __name__ == '__main__':
    # Use port 8000 as it's a common default
    app.run(host='0.0.0.0', port=8000, debug=True)