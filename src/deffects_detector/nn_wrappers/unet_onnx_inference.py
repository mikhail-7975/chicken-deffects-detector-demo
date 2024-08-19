from typing import Any
import onnxruntime as ort


class UnetModel:
    def __init__(self, model_path, preprocessing=None, postprocessing=None):
        self.central_body_segmentation_model = \
            ort.InferenceSession(model_path)

    def __call__(self, input_image) -> Any:
        pass