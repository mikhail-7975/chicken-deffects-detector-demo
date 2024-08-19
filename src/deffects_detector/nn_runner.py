from typing import List
from typing import Dict

import numpy as np

from deffects_detector.nn_wrappers.unet_onnx_inference import UnetModel
from deffects_detector.nn_wrappers.yolo_onnx_inference import YoloV8Model

class NNRunner:
    def __init__(
            self, 
            body_segmentation_model_path,
            hematomes_segmentation_model_path,
            deffects_detection_model_path
        ):
        self.central_body_segmentation_model = \
            UnetModel(body_segmentation_model_path)
        self.hematomes_segmentation_model = \
            UnetModel(hematomes_segmentation_model_path)
        self.deffects_detection_model = \
            YoloV8Model(deffects_detection_model_path)

        
    def __call__(self, chicken_image: np.ndarray) -> Dict:
        # 0. Select central body
        central_body_heatmap = self.central_body_segmentation_model(chicken_image)

        # 1. Detection
        detection_raw_out = [
            {
                "type": "",
                "bbox": "",
                "confidence": ""
            }
        ]

        # 1.1 Postprocessing: 
        # - check if detection out in deffects list
        # - localize
        # - append to detection_postprocessed_result

        detection_postprocessed_result = [
            {
                "deffect_type":"open_brek",
                "bbox": [], # xywh
                "segmentation": [], #xyxyxy
                "localization": "right_wing"
            },

        ]

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