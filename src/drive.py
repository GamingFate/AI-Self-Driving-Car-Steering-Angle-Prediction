import os
import cv2
import numpy as np
import socketio
import eventlet
import eventlet.wsgi
from flask import Flask
from tensorflow.keras.models import load_model
from PIL import Image
from io import BytesIO
import base64

# ─────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────
MODEL_PATH = r"F:\major project 8th sem\Self Driving Car\Mboth1_2_2nd.h5"
IMG_HEIGHT  = 66
IMG_WIDTH   = 200
SPEED_LIMIT = 20

# ─────────────────────────────────────────
# LOAD MODEL
# ─────────────────────────────────────────
print("Loading model...")
model = load_model(MODEL_PATH)
print("✅ Model loaded!")

# ─────────────────────────────────────────
# FLASK + SOCKETIO
# ─────────────────────────────────────────
sio = socketio.Server()
app = Flask(__name__)
app = socketio.Middleware(sio, app)

# ─────────────────────────────────────────
# PREPROCESS IMAGE
# ─────────────────────────────────────────
def preprocess(img):
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
    img = img.astype(np.float32)
    # NOTE: No normalization here — model's Lambda layer handles it
    return img

# ─────────────────────────────────────────
# SOCKETIO EVENTS
# ─────────────────────────────────────────
prev_steering = 0.0  # global state

@sio.on('connect')
def connect(sid, environ):
    print("✅ Simulator connected!")
    send_control(0, 0)

@sio.on('telemetry')
def telemetry(sid, data):
    global prev_steering  # fix: declare global

    if data:
        speed = float(data['speed'])

        # Decode image
        img = Image.open(BytesIO(base64.b64decode(data['image'])))
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # Preprocess + predict steering
        processed = preprocess(img)
        processed = np.expand_dims(processed, axis=0)
        steering = float(model.predict(processed, verbose=0)[0][0])

        # Smooth steering
        steering = 0.7 * prev_steering + 0.3 * steering
        prev_steering = steering

        # Clamp steering to valid range
        steering = max(min(steering, 1.0), -1.0)

        # Tiered throttle control
        if speed < 10:
            throttle = 0.4
        elif speed < SPEED_LIMIT:
            throttle = 0.25
        else:
            throttle = 0.1

        print(f"Steering: {steering:.4f} | Throttle: {throttle:.2f} | Speed: {speed:.2f}")
        send_control(steering, throttle)

def send_control(steering, throttle):
    sio.emit('steer', data={
        'steering_angle': str(steering),
        'throttle': str(throttle)
    })

# ─────────────────────────────────────────
# RUN SERVER
# ─────────────────────────────────────────
if __name__ == '__main__':
    print("🚗 Starting autonomous driving server...")
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
    


