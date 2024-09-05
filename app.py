from flask import Flask, render_template
from flask_socketio import SocketIO
from datetime import datetime
import random

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_send_message(username, message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    full_message = f"{timestamp} - {username}: {message}"
    socketio.emit('receive_message', full_message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
