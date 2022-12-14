from flask import Flask # Importing Flask libraries.
from flask_socketio import SocketIO # Importing the Flask-SocketIO library.

app = Flask(__name__) # Creating an instance of a Flask application
app.config['SECRET_KEY'] = 'secret!' # Creating a secret key to encrypt user sessions
socketio = SocketIO(app) # Wrapping the instance of the Flask application,
                         # with the SocketIO class to give it access to
                         # SocketAPI features through SocketIO.

@app.route("/") # When a client connects to 127.0.0.1:XXXX/...
def index():
    print("Succesful connection") # Print this message in the console.
    return "<h1>Test Page</h1>" # Render this HTML code on the page.

if __name__ == '__main__':
    socketio.run(app) # Allows the Python script to access Flask functionality
                      # and Flask-SocketIO functionality when it is executed.
