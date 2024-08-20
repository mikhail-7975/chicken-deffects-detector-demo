import json

import cv2
import numpy as np

from src.deffects_detector.nn_wrappers.yolo_onnx_inference import Yolov8Onnx
from src.deffects_detector.utils.highlight import draw_detections

def test_valid_segmentation():
    model = Yolov8Onnx('data/model_weights/yolov8_640x640_chicken_deffects_base.onnx', 
                       confidence_thres=0.05, 
                       iou_thres=0.2)
    
    inp_img = cv2.imread('data/raw_images/img_7020570882495152157.jpg')
    result = model(inp_img[:, :, ::-1])
    assert result is not None

    result_json = []
    for res in result:
        result_json.append({
            'box': res['box'],
            'score': str(res['score']),
            'class_id': str(res['class_id'])
        })
    
    with open("tmp/detection_results.json", 'w') as f:
        json.dump(result_json, f, separators=(',\n', ': '))

    color_palette = [
        (0, 0, 0),
        (255, 255, 255),
        (0, 255, 0),
        (255, 255, 0),
        (255, 0, 0),
        (255, 0, 255),
        (255, 255, 255),
        (127, 127, 255),
    ]
    # plt.imshow(inp_img)
    for res in result:
        draw_detections(inp_img, res['box'], float(res['score']), int(res['class_id']), color_palette)
    
    cv2.imwrite("tmp/detection_test.jpg", inp_img)