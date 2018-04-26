import socket
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello! I am a Flask application.'

@app.route('/env')
def print_env():
    return socket.gethostbyname(socket.gethostname())

@app.route('/<path:full_path>')
def print_path(full_path):
    ip = socket.gethostbyname(socket.gethostname())
    return 'Hello! I am a Flask application on %s. Request path: %s' % (ip, full_path)

if __name__ == '__main__':
    # Note the extra host argument. If we didn't have it, our Flask app
    # would only respond to requests from inside our container
    app.run(host='0.0.0.0')
