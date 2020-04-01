from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@socketio.on('connection')
def handle_message(message):
    print('user connected')

@socketio.on('disconnection')
def handle_message(message):
    print('user disconnected')

@socketio.on('chat message')
def handle_message(message):
    emit('chat message', message,broadcast=True)

if __name__ == '__main__':
    socketio.run(app)




