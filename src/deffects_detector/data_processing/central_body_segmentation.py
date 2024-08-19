import albumentations as A
import numpy as np

from .prepostprocessing_base import ProcessingBase

class BodySegmentationProcessing(ProcessingBase):
    def __init__(self):
        self.transforms = A.Compose([
            A.Resize(128, 128),
            A.Normalize(),
        ])
    
    def preproccess(self, data):
        return np.zeros((1, 3, 128, 128))
    
    def postprocess(self, data):
        return np.zeros((695, 519, 3), dtype=np.uint8)