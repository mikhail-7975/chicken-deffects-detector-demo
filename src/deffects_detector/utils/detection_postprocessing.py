

def split_deffects(raw_deffects_list):
    legs = []
    wings = []
    hematomes = []

    for detected in raw_deffects_list:
        if detected['class_id'] in [2, 3]:
            legs.append(detected)
        if detected['class_id'] in [4, 5, 6]:
            wings.append(detected)
        if detected['class_id'] in [7]:
            hematomes.append(detected)
    
    legs.sort(key=lambda item:item['box'][0])
    wings.sort(key=lambda item:item['box'][0])
    return legs, wings, hematomes

def is_bbox_center_inside(bbox1, bbox2):
    """
    Check if the center of bbox1 is inside bbox2.
    
    bbox1 and bbox2 are tuples in the format (x_min, y_min, x_max, y_max)
    """
    # Calculate the center of bbox1
    center_x = bbox1[0] + bbox1[2] / 2
    center_y = bbox1[1] + bbox1[3] / 2
    
    # Check if the center is inside bbox2
    return (bbox2[0] <= center_x <= bbox2[0] + bbox2[2]) \
        and (bbox2[1] <= center_y <= bbox2[1] + bbox2[3])

def add_hematome_localization(hematomes_list, legs, wings):
    for i, hematome in enumerate(hematomes_list):
        hematomes_list[i]['localization'] = "body"
        hematome_box = hematome['box']
        if is_bbox_center_inside(hematome_box, legs[0]['box']):
            hematomes_list[i]['localization'] = "left leg"
        if is_bbox_center_inside(hematome_box, legs[1]['box']):
            hematomes_list[i]['localization'] = "right leg"
        if is_bbox_center_inside(hematome_box, wings[0]['box']):
            hematomes_list[i]['localization'] = "left wing"
        if is_bbox_center_inside(hematome_box, wings[1]['box']):
            hematomes_list[i]['localization'] = "right wing"
        