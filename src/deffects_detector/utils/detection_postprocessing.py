

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
