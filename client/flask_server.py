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

@app.route('/', methods=['GET'])
def hello_world():
    # data = json.loads(request.get_data())
    # data = request.get_data()
    # print("args", request.args)
    # print("data", request.get_data())
    # with open("data.json", 'w') as f:
    #     json.dump(data)
    # message=b"request from / "
    # socket.send(message)

    # #  Get the reply.
    # message = socket.recv()
    return jsonify({'resp':'response from flask'}) # + message.decode('utf-8')

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