import sys
sys.path.insert(0, '/home/acer/Documents/flask-practice')
from video_stream import create_app


if __name__ == "__main__":
    socketio, app = create_app()
    socketio.run(app, port=9487, host='0.0.0.0', debug=True)   