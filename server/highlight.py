import cv2
import numpy as np

COLOR_PALETTE = [
    (0, 0, 0),
    (255, 255, 255), # chicken_body
    (0, 255, 0), #leg fixed
    (255, 255, 0), # leg not fixed
    (0, 255, 0), # normal wing
    (255, 255, 0), # closed break
    (255, 0, 0), # open break
    (255, 0, 255), # hematome
]

DETECT_NAMES = [
    "",
    "body",
    "leg fixed",
    "leg not fixed",
    "normal wing",
    "closed break",
    "open break",
    "hematome"
]

def draw_detections(img, box, score, class_id, 
                    color_palette, class_names):
    """
    Draws bounding boxes and labels on the input image based on the detected objects.

    Args:
        img: The input image to draw detections on.
        box: Detected bounding box.
        score: Corresponding detection score.
        class_id: Class ID for the detected object.

    Returns:
        None
    """
    x1, y1, w, h = box
    color = color_palette[class_id]
    cv2.rectangle(img, (int(x1), int(y1)), (int(x1 + w), int(y1 + h)), color, 2)
    label = f"{class_names[class_id]}"
    (label_width, label_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    label_x = x1
    label_y = y1 - 10 if y1 - 10 > label_height else y1 + 10
    cv2.rectangle(
        img, (label_x, label_y - label_height), (label_x + label_width, label_y + label_height), color, cv2.FILLED
    )
    cv2.putText(img, label, (label_x, label_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

