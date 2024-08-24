import json
import base64

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

@app.route('/image', methods=['GET'])
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
    
    with open('tmp/nn_runner_test_7020570882494890022.jpg', mode='rb') as file:
        img = file.read()   
    # Create a response dictionary
    encoded_image = base64.encodebytes(img).decode('utf-8')
    response_data = {
        "image": encoded_image,
        "body": [
            {
                "defect_type":"hematome",
                "message":"Гематомаы",
                "color": "yellow"

            }
        ],
        "left_leg": [],
        "right_leg": [
            {
                "defect_type":"leg_not_fixed",
                "message":"нога не зафиксирована",
                "color": "yellow"
            }
        ],
        "left_wing": [
            {
                "defect_type":"open_break",
                "message":"открытый перелом",
                "color": "red"
            }
        ],
        "right_wing": [
            {
                "defect_type":"closed_break",
                "message":"закрытый перелом",
                "color":"yellow"
            }
        ],
        "decision":"A"
    }
    print(method)
    with open("tmp/nn_runner_etalon_json_7020570882494890022.json", 'w') as f:
        json.dump(response_data, f)
    return jsonify(response_data) # + message.decode('utf-8')


if __name__ == '__main__':
    app.run(debug=True)