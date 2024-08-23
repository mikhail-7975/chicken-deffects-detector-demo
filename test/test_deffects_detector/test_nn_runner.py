import json
from pathlib import Path

import cv2
import numpy as np

from src.deffects_detector.nn_runner import NNRunner
from src.deffects_detector.utils.highlight import draw_detections

def test_valid_nn_runner():
    runner = NNRunner(
        body_segmentation_model_path='data/model_weights/unet_500_imgs_50_epoch_all_classes.onnx',
        hematomes_segmentation_model_path='',
        deffects_detection_model_path='data/model_weights/yolov8_640x640_chicken_deffects_base.onnx',
    )
    test_images = ['data/raw_images/img_7020570882494890022.jpg']
    # test_images = list(map(str, Path('data/raw_images').glob("*.jpg")))
    for img_path in test_images:
        inp_img = cv2.imread(img_path)
        result = runner(inp_img[:, :, ::-1])
        assert result is not None
        out_image, detection_result, processed_result = result
        color_palette = [
            (0, 0, 0),
            (255, 255, 255), # chicken_body
            (0, 255, 0), #leg fixed
            (255, 255, 0), # leg not fixed
            (0, 255, 0), # normal wing
            (255, 255, 0), # closed break
            (255, 0, 0), # open break
            (255, 0, 255), # hematome
        ]
        # plt.imshow(inp_img)
        detect_names = [
            "",
            "body",
            "leg fixed",
            "leg not fixed",
            "normal wing",
            "closed break",
            "open break",
            "hematome"
        ]

        for res in detection_result:
            draw_detections(out_image, res['box'], res['score'], res['class_id'], 
                            color_palette, detect_names)
        
        cv2.imwrite(f"tmp/nn_runner_test_{img_path.split('_')[-1]}", out_image[:, :, ::-1])
        with open(f"tmp/nn_runner_test_{img_path.split('_')[-1]}.json", 'w') as f:
            json.dump(processed_result, f, skipkeys=True)