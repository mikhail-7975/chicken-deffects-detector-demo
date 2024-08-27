import json
import base64
from pathlib import Path

import cv2
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

from src.deffects_detector.nn_runner import NNRunner
from src.deffects_detector.utils.detection_postprocessing import add_hematome_localization
from src.deffects_detector.utils.detection_postprocessing import split_deffects
from src.deffects_detector.utils.highlight import draw_detections
from server.deffect_messages import DEFFECT_IDS
from server.deffect_messages import nn_out_to_fronted_format
from server.highlight import DETECT_NAMES, COLOR_PALETTE

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def root():
    return "root"

class ImageFolderSource:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.image_paths = list(map(str, Path(image_folder).glob('*.jpg')))
        print(f"found {len(self.image_paths)} images")
        self.image_i = 0

    def get_next_path(self):
        self.image_i = (self.image_i + 1) % len(self.image_paths)
        return  self.image_paths[self.image_i]

    def get_prev_path(self):
        self.image_i -= 1
        if self.image_i < 0:
            self.image_i = len(self.image_paths) - 1
        return  self.image_paths[self.image_i]

img_folder_source = ImageFolderSource('data/raw_images')
runner = NNRunner(
        body_segmentation_model_path='data/model_weights/unet_500_imgs_50_epoch_all_classes.onnx',
        hematomes_segmentation_model_path='',
        deffects_detection_model_path='data/model_weights/yolov8_640x640_chicken_deffects_base.onnx',
    )


@app.route('/image', methods=['GET'])
def hello_world():
    # Parse JSON payload
    json_data = request.get_json(silent=True)
    button_type = request.args.get('type')
    print("button_type", button_type)

    if button_type == "next":
        img_path = img_folder_source.get_next_path()
    else:
        img_path = img_folder_source.get_prev_path()

    print(img_path)
    with open(img_path, mode='rb') as file:
        img = file.read()   
    # Create a response dictionary
    
    inp_img = cv2.imread(img_path)
    result = runner(inp_img[:, :, ::-1])
    out_image, raw_deteciton_result, processed_result = result
    
    for res in raw_deteciton_result:
        draw_detections(inp_img, res['box'], res['score'], res['class_id'], 
                        COLOR_PALETTE, DETECT_NAMES)

    cv2.imwrite("tmp/image_to_send.jpg", inp_img)

    detected_only_deffects = [i for i in raw_deteciton_result if i['class_id'] in DEFFECT_IDS]
    
    legs, wings, hematomes = split_deffects(raw_deteciton_result)
    add_hematome_localization(hematomes, legs, wings)


    with open('tmp/image_to_send.jpg', mode='rb') as file:
        img = file.read()   
    encoded_image = base64.encodebytes(img).decode('utf-8')
    
    response_data = {}
    for k in processed_result.keys():
        # result_for_frontend = []
        if k not in response_data.keys():
            response_data[k] = []
        response_data[k] = [nn_out_to_fronted_format(n) for n in processed_result[k]]

    response_data["image"] = encoded_image

    detected_deffect_ids = [i['class_id'] for i in raw_deteciton_result]

    quality_class = "A"

    if 7 in detected_deffect_ids or 5 in detected_deffect_ids:
        quality_class = "B"

    if 6 in detected_deffect_ids:
        quality_class = "C"

    response_data["decision"]=quality_class

    __response_data = {
        "image": encoded_image,
        "body": [
            {
                "defect_type":"hematome",
                "message":"Гематомаы",
                "color": "yellow"
            }#,
            # {
            # "box": [
            #     205,
            #     242,
            #     31,
            #     46
            # ],
            # "score": 0.6587011814117432,
            # "class_id": 7,
            # "localization": "body"
            # }
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

    with open("tmp/nn_runner_etalon_json_7020570882494890022.json", 'w') as f:
        json.dump(response_data, f)
    return jsonify(response_data) # + message.decode('utf-8')

def main():
    runner = NNRunner(
        body_segmentation_model_path='data/model_weights/unet_500_imgs_50_epoch_all_classes.onnx',
        hematomes_segmentation_model_path='',
        deffects_detection_model_path='data/model_weights/yolov8_640x640_chicken_deffects_base.onnx',
    )

    with open('data/raw_images/img_7020570882494890022.jpg', mode='rb') as file:
        img = file.read()   
    # Create a response dictionary
    
    inp_img = cv2.imread('data/raw_images/img_7020570882494890022.jpg')
    result = runner(inp_img[:, :, ::-1])
    out_image, raw_deteciton_result, processed_result = result
    
    detected_only_deffects = [i for i in raw_deteciton_result if i['class_id'] in DEFFECT_IDS]
    
    legs, wings, hematomes = split_deffects(raw_deteciton_result)
    add_hematome_localization(hematomes, legs, wings)

    encoded_image = base64.encodebytes(img).decode('utf-8')
    
    response_data = {}
    for k in processed_result.keys():
        # result_for_frontend = []
        if k not in response_data.keys():
            response_data[k] = []
        response_data[k] = [nn_out_to_fronted_format(n) for n in processed_result[k]]

    print(response_data)

if __name__ == '__main__':
    # main()
    app.run(debug=True)