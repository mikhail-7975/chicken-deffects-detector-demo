import cv2

from src.deffects_detector.nn_wrappers.unet_onnx_inference import UnetModel
from src.deffects_detector.data_processing.central_body_segmentation import BodySegmentationProcessing

def test_valid_segmentation():
    processing = BodySegmentationProcessing()
    model = UnetModel('data/model_weights/unet_500_imgs_50_epoch_all_classes.onnx',
                      processing.preproccess,
                      processing.postprocess)
    
    inp_img = cv2.imread('data/raw_images/img_7020570882494890022.jpg')[:, :, ::-1]
    result = model(inp_img)
    cv2.imwrite("tmp/segmentation_test.jpg", result[:, :, ::-1])
    assert result is not None

