import time
import threading
import base64
import queue
from collections import deque

import cv2
from flask import current_app, Blueprint, render_template
vs = Blueprint('video', __name__, template_folder='templates', static_folder='static', static_url_path='/video/static')
from flask_socketio import emit

from video_stream import socketio

import socket    


class _Image:
    def __init__(self):
        self.image = deque(maxlen=10)
    def add(self, data):
        self.image.append(data)
    def pop(self):
        return self.image[0]
Image = _Image()

def cam():
    cap = cv2.VideoCapture('rtsp://admin:hk888888@10.36.172.101:554/Streaming/Channels/001')
    while True:
        ret, frame = cap.read()
        assert ret
        Image.add(frame)
threading.Thread(target=cam, daemon=True).start()


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

@vs.route('/video_stream')
def index():
    ip = get_ip_address()
    return render_template('index.html', ip=ip, port=9487)

@socketio.on('connect', namespace='/stream')
def connect():
    emit('response', {'data': 'Connected'})

@socketio.on('stream', namespace='/stream')
def stream(msg):
    msg = {}
    try:
        frame = Image.pop()
        encoded_frame = cv2.imencode('.jpg', frame)[1]
        base64_data = base64.b64encode(encoded_frame)
        data_string = base64_data.decode()
        frame = f'data:image/jpeg;base64,{data_string}'
        msg = {'status': True, 'data': frame}
    except:
        msg = {'status': False, 'data': None}
    emit('stream', msg)

@socketio.on('disconnect', namespace='/stream')
def disconnect():
    emit('response', {'data': 'Disconnected'})


# if __name__ == '__main__':
    # threading.Thread(target=streaming, daemon=True).start()
    # socketio.run(app)
    # stream.set()
    # camera()