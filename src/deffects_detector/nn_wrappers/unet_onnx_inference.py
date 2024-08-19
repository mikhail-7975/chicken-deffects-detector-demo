from typing import Any
import onnxruntime as ort


class UnetModel:
    def __init__(self, model_path, preprocessing=None, postprocessing=None):
        self.session = \
            ort.InferenceSession(model_path)
        
        self.input_name = self.session.get_inputs()[0].name

        self.preprocessing = preprocessing
        self.postprocessing = postprocessing

    def __call__(self, input_image) -> Any:
        '''
        input_image - raw image with shape (h, w, c) and uint8 dtype
        '''
        if self.preprocessing is None:
            raise Exception("UnetModel: preprocessing is not defined")
        if self.postprocessing is None:
            raise Exception("UnetModel: postprocessing is not defined")

        input_data = self.preprocessing(input_image)
        if input_data.max() == 0:
            raise Exception("UnetModel: zero value input")
        model_out = self.session.run(None, {self.input_name: input_data})[0]
        result = self.postprocessing(model_out, input_image)
        return result