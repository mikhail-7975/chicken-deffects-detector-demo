import json
from src.deffects_detector.utils.detection_postprocessing import split_deffects
from src.deffects_detector.utils.detection_postprocessing import add_hematome_localization


def test_split_deffects():
    with open('data/test_files/detection_results.json', 'r') as f:
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


def test_hematomes_localization():
    with open('data/test_files/legs.json', 'r') as f:
        legs = json.load(f)
    with open('data/test_files/wings.json', 'r') as f:
        wings = json.load(f)
    with open('data/test_files/hematomes.json', 'r') as f:
        hematomes = json.load(f)
    add_hematome_localization(hematomes, legs, wings)
    for h in hematomes:
        assert 'localization' in h.keys()
    with open('tmp/hematomes_winth_localization.json', 'w') as f:
        json.dump(hematomes, f)