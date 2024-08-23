import json
from src.deffects_detector.utils.detection_postprocessing import split_deffects

def test_split_deffects():
    with open('data/test_files/raw_detection_results.json', 'r') as f:
        detection_out = json.load(f)
    leg, wings, hematomes = split_deffects(detection_out)
    assert detection_out is not None
    assert leg is not None
    assert wings is not None
    assert hematomes is not None
    
    assert len(leg) == 2
    assert len(wings) == 2

    assert leg[0]['box'][0] < leg[1]['box'][0]
    assert wings[0]['box'][0] < wings[1]['box'][0]
    
    with open('tmp/legs.json', 'w') as f:
        json.dump(leg, f)
    with open('tmp/wings.json', 'w') as f:
        json.dump(wings, f)
    with open('tmp/hematomes.json', 'w') as f:
        json.dump(hematomes, f)