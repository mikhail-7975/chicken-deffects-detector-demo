import albumentations as A
import cv2
import numpy as np

from .prepostprocessing_base import ProcessingBase

class BodySegmentationProcessing(ProcessingBase):
    def __init__(self):
        self.nn_inp_height = 704
        self.nn_inp_width = 544
        self.transforms = A.Compose([
            A.Resize(self.nn_inp_height, self.nn_inp_width),
            A.Normalize(),
        ])
    
    def preproccess(self, *args, **kwargs):
        input_image = kwargs.get('image', None)
        if len(args) >= 1:
            input_image = args[0]
        else:
            input_image = None

        
        if input_image is None:
            raise Exception("BodySegmentationProcessing: input image is None")

        transformed = self.transforms(image=input_image)['image']
        transposed = transformed.transpose(2, 0, 1)[None]
        return transposed
    
    def postprocess(self, *args, **kwargs):
        heatmap = kwargs.get('heatmap', None)
        if len(args) >= 1:
            heatmap = args[0]
            input_image = args[1]
        else:
            heatmap = None
            input_image = None

        heatmap = heatmap[0, 0]
        
        if heatmap is None:
            raise Exception("BodySegmentationProcessing: heatmap is None")
        if input_image is None:
            raise Exception("BodySegmentationProcessing: input_image is None")

        binary = (heatmap > 0.2).astype(np.uint8)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        largest_contour = max(contours, key=cv2.contourArea)
        largest_contour = largest_contour / (self.nn_inp_width, self.nn_inp_height)
        largest_contour *= (519, 695)
        largest_contour = largest_contour.astype(np.int32)

        mask = np.zeros((695, 519, 3))
        cv2.drawContours(mask, [largest_contour], -1, (1, 1, 1), -1)
        
        return  (input_image * mask).astype(np.uint8)