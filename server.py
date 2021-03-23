import socketio
import time
from flask import Flask
import eventlet
import eventlet.wsgi

sio = socketio.Server()
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

@sio.on('connect')
def on_connect(a, b):
    print("Connected")
    sio.emit('event_name', {'data': 'test'})

@sio.on('event_name')
def handle_message(_sid, data):
    print(f"recieved: {data}")
    time.sleep(3)
    sio.emit('event_name', {'data': 'sent from server'})

if __name__ == '__main__':
    print("starting server")
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)
