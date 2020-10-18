import time
import threading
import base64
import queue

import cv2
from flask import current_app, Blueprint, render_template
vs = Blueprint('video', __name__, template_folder='templates', static_folder='static', static_url_path='/video/static')
from flask_socketio import emit

from video_stream import socketio

import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 
cap = cv2.VideoCapture(0)

@vs.route('/video_stream')
def index():
    return render_template('index.html', ip=IPAddr, port=9487)

@socketio.on('connect', namespace='/stream')
def connect():
    emit('response', {'data': 'Connected'})

@socketio.on('stream', namespace='/stream')
def stream(msg):
    msg = {}
    try:
        ret, frame = cap.read()
        assert ret
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