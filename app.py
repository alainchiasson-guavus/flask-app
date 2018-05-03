import socket
import os
from flask import Flask,request

# if "TAG" in os.environ:
#     tag = os.getenv('TAG')
tag = os.getenv('TAG', 'default')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '%s : Hello! I am a Flask application.' % tag

@app.route('/env')
def print_env():
    return '%s : %s' % (tag, socket.gethostbyname(socket.gethostname()))

@app.route('/<path:full_path>')
def print_path(full_path):
    ip = socket.gethostbyname(socket.gethostname())
    return '%s : Hello! I am a Flask application on %s. Request path: %s' % (tag, ip, full_path)

if __name__ == '__main__':
    # Note the extra host argument. If we didn't have it, our Flask app
    # would only respond to requests from inside our container
    app.run(host='0.0.0.0')
