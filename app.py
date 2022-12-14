from flask import Flask, render_template # Importing Flask libraries.
from flask_socketio import SocketIO # Importing the Flask-SocketIO library.

app = Flask(__name__) # Creating an instance of a Flask application
app.config['SECRET_KEY'] = 'secret!' # Creating a secret key to encrypt user sessions
socketio = SocketIO(app) # Wrapping the instance of the Flask application,
                         # with the SocketIO class to give it access to
                         # SocketAPI features through SocketIO.

@app.route("/") # When a client connects to 127.0.0.1:XXXX/...
def index():
    return render_template('index.html', async_mode=socketio.async_mode) # Serve the client index.html from the 'templates' directory.

@socketio.on('connect') # When a 'connect' WebSocket event is recieved from the backend...
def handle_connection():
    socketio.emit('announceUserConnect') # Send an 'announceUserConnect' WebSocket event to the
                                         # JavaScript backend, for all users currently connected
                                         # to the webpage.

@socketio.on('disconnect') # When a 'disconnect' WebSocket event is recieved from the backend...
def handle_disconnect():
    socketio.emit('announceUserDisconnect') # Send an 'announceUserDisconnect' WebSocket event to the
                                            # JavaScript backend.

@socketio.on('recieve_message') # When a 'recieve_message' WebSocket event is recieved from the backend...
def handle_message(data):
    print(data) # Output the contents of the message that was sent to the terminal
    socketio.emit('addMessageToFeed', data) # Send an 'addMessageToFeed' WebSocket event to the
                                            # JavaScript backend. This event contains the message
                                            # that was sent by the user.

if __name__ == '__main__':
    socketio.run(app) # Allows the Python script to access Flask functionality
                      # and Flask-SocketIO functionality when it is executed.
