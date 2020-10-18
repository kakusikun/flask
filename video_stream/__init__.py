import logging
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    print(__name__)
    app = Flask(__name__.split('.')[0])
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.config['SECRET_KEY'] = '2684251e19d3d6f2ecc5acf672272e43'
    app.config['RESTFUL_JSON'] = {'ensure_ascii': False}
    
    from video_stream.stream import vs
    app.register_blueprint(vs)
    socketio.init_app(app)
    return socketio, app