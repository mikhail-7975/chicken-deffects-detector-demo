from typing import Any

import cv2
import numpy as np
import onnxruntime as ort


class Yolov8Onnx:
    """YOLOv8 object detection model class for handling inference and visualization."""

    def __init__(self, onnx_model, confidence_thres, iou_thres):
        """
        """
        self.onnx_model = onnx_model
        self.confidence_thres = confidence_thres
        self.iou_thres = iou_thres

        # Load the class names from the COCO dataset
        self.classes = [str(i) for i in range(10)]
        self.session = ort.InferenceSession(self.onnx_model, providers=["CUDAExecutionProvider", "CPUExecutionProvider"])
        
        self.model_inputs = self.session.get_inputs()
        input_shape = self.model_inputs[0].shape
        self.input_width = input_shape[2]
        self.input_height = input_shape[3]


    def preprocess(self, raw_image):
        """
        raw_image - np.array with shape (h, w, c) and dtype np.uint8
        """
        img = cv2.resize(raw_image, (self.input_width, self.input_height))
        image_data = np.array(img) / 255.0
        image_data = np.transpose(image_data, (2, 0, 1))  # Channel first
        image_data = np.expand_dims(image_data, axis=0).astype(np.float32)
        return image_data

    def postprocess(self, input_image, output, draw_deffects=True):
        """
        input_image (numpy.ndarray): The input image.
        output (numpy.ndarray): The output of the model.
        """
        outputs = np.transpose(np.squeeze(output[0]))
        rows = outputs.shape[0]

        boxes = []
        scores = []
        class_ids = []

        img_height, img_width, ch = input_image.shape
        x_factor = img_width / self.input_width
        y_factor = img_height / self.input_height

        for i in range(rows):
            classes_scores = outputs[i][4:]
            max_score = np.amax(classes_scores)
            if max_score >= self.confidence_thres:
                class_id = np.argmax(classes_scores)
                x, y, w, h = outputs[i][0], outputs[i][1], outputs[i][2], outputs[i][3]
                left = int((x - w / 2) * x_factor)
                top = int((y - h / 2) * y_factor)
                width = int(w * x_factor)
                height = int(h * y_factor)

                class_ids.append(class_id)
                scores.append(max_score)
                boxes.append([left, top, width, height])

        indices = cv2.dnn.NMSBoxes(boxes, scores, self.confidence_thres, self.iou_thres)

        detection_results = []
        for i in indices:
            box = boxes[i]
            score = scores[i]
            class_id = class_ids[i]
            detection_results.append(
                {
                    "box": box,
                    "score": score,
                    "class_id": class_id
                }
            )

        return detection_results
    
    def __call__(self, image):
        
        # session = ort.InferenceSession(self.onnx_model, providers=["CUDAExecutionProvider", "CPUExecutionProvider"])

        # Get the model inputs
        

        img_data = self.preprocess(image)
        outputs = self.session.run(None, {self.model_inputs[0].name: img_data})
        detection_result = self.postprocess(image, outputs, draw_deffects=False) 
        return detection_result