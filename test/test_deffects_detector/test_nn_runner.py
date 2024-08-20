import json

import cv2
import numpy as np

from src.deffects_detector.nn_runner import NNRunner
from src.deffects_detector.utils.highlight import draw_detections

def test_valid_nn_runner():
    runner = NNRunner(
        body_segmentation_model_path='data/model_weights/unet_50_epoch_all_classes.onnx',
        hematomes_segmentation_model_path='',
        deffects_detection_model_path='data/model_weights/yolov8_640x640_chicken_deffects_base.onnx',
    )
    inp_img = cv2.imread('data/raw_images/img_7020570882494759032.jpg')
    result = runner(inp_img[:, :, ::-1])
    assert result is not None
    out_image, detection_result = result
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
    for res in detection_result:
        draw_detections(out_image, res['box'], res['score'], res['class_id'], color_palette)
    
    cv2.imwrite("tmp/nn_runner_test.jpg", out_image[:, :, ::-1])