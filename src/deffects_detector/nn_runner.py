import json
from typing import List
from typing import Dict

import numpy as np

from src.deffects_detector.nn_wrappers.unet_onnx_inference import UnetModel
from src.deffects_detector.nn_wrappers.yolo_onnx_inference import Yolov8Onnx
from src.deffects_detector.data_processing.central_body_segmentation import BodySegmentationProcessing


class NNRunner:
    def __init__(
            self, 
            body_segmentation_model_path,
            hematomes_segmentation_model_path,
            deffects_detection_model_path
        ):

        self.body_segmentation_processing = BodySegmentationProcessing()
        
        self.central_body_segmentation_model = \
            UnetModel(body_segmentation_model_path, 
                      self.body_segmentation_processing.preproccess,
                      self.body_segmentation_processing.postprocess)
        # self.hematomes_segmentation_model = \
        #     UnetModel(hematomes_segmentation_model_path)
        self.deffects_detection_model = \
            Yolov8Onnx(deffects_detection_model_path,
                       confidence_thres=0.05, 
                       iou_thres=0.2)

        
    def __call__(self, chicken_image: np.ndarray) -> Dict:
        # 0. Select central body
        central_body_image = self.central_body_segmentation_model(chicken_image)
        detection_raw_out = self.deffects_detection_model(central_body_image)

        
        
        # with open("legs.json") as f:
        #     json.dump(legs)
        # with open("wings.json") as f:
        #     json.dump(wings)
        return central_body_image, detection_raw_out
        # detection_raw_out = [
        #     {
        #         "box": [299, 351, 113, 109],
        #         "score": "0.9612121",
        #         "class_id": "4"
        #     },
        # ]

        # 1.1 Postprocessing: 
        # - check if detection out in deffects list
        # - localize
        # - append to detection_postprocessed_result

        
        # 2. Split to final dict with result

        result = {
            "body": [

            ],
            "left_leg": [

            ],
            "right_leg": [

            ],
            "left_wing": [

            ],
            "right_wing": [

            ]
        }
        pass