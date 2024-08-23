import json
from typing import List
from typing import Dict

import numpy as np

from src.deffects_detector.nn_wrappers.unet_onnx_inference import UnetModel
from src.deffects_detector.nn_wrappers.yolo_onnx_inference import Yolov8Onnx
from src.deffects_detector.data_processing.central_body_segmentation import BodySegmentationProcessing 
from src.deffects_detector.utils.detection_postprocessing import split_deffects
from src.deffects_detector.utils.detection_postprocessing import add_hematome_localization

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

        
        legs, wings, hematomes = split_deffects(detection_raw_out)
        add_hematome_localization(hematomes, legs, wings)
        
        result = {
            "body": [h for h in hematomes if h['localization'] == 'body'],
            "left_leg": [legs[0]] + \
                [h for h in hematomes if h['localization'] == 'left leg'],
            "right_leg": [legs[1]] + \
                [h for h in hematomes if h['localization'] == 'right leg'],
            "left_wing": [wings[0]] + \
                [h for h in hematomes if h['localization'] == 'left wing'],
            "right_wing":  [wings[1]] + \
                [h for h in hematomes if h['localization'] == 'right wing']
        }
        return central_body_image, detection_raw_out, result
        