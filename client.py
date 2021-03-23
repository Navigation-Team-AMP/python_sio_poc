import socketio
import time

sio = socketio.Client()

@sio.on('event_name')
def handle_message(data):
    print(f"recieved: {data}")
    time.sleep(3)
    sio.emit('event_name', {'data': 'sent from client'})

@sio.on('connect')
def on_connect():
    print("Connected")

if __name__ == '__main__':
    sio.connect('http://127.0.0.1:5000')
