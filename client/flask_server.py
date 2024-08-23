import json

from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def root():
    return "root"

@app.route('/post-example', methods=['POST'])
def hello_world():
    query_params = request.args.to_dict()
    
    # Parse form data
    form_data = request.form.to_dict()
    
    # Parse JSON payload
    json_data = request.get_json(silent=True)
    
    # Parse headers
    headers = dict(request.headers)
    
    # Parse URL
    url = request.url
    
    # Parse method
    method = request.method
    
    # Parse cookies
    cookies = request.cookies.to_dict()
    
    # Create a response dictionary
    response_data = {
        'method': method,
        'answer': 'hello world from post-example!'
    }
    print(method)
    return jsonify(response_data) # + message.decode('utf-8')

# @app.route('/image', methods=['POST'])
# def hello_world_image():
#     data = request.get_json(force=True)
#     with open("data.json", 'w') as f:
#         json.dump(data)
#     message=b"request from / image"
#     socket.send(message)

#     #  Get the reply.
#     message = socket.recv()
#     return 'Hello, World!' + message.decode('utf-8')

if __name__ == '__main__':
    app.run(debug=True)