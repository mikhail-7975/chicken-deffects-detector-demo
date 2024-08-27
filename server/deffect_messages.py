CLASS_NAMES = [
    '',
    'body',
    'leg_fixed',
    'leg_not_fixed',
    'normal_wing',
    'closed_break',
    'open_break',
    'hematome',
]

MESSAGES = [
    '',
    '',
    '',
    'нога не зафиксирована',
    '',
    'закрытый перелом',
    'открытый перелом',
    'гематома',
]

DEFFECT_IDS = [3, 5, 6, 7]

NAMES_TRANSLATION = [
    '',
    '',
    'нога зафиксирована',
    'нога не зафиксирована',
    '',
    'закрытый перелом',
    'открытый перелом',
    'гематома'
]

colors = [
    'green',
    'green',
    'green',
    'yellow',
    'green',
    'yellow',
    'red',
    'yellow',
]

def nn_out_to_fronted_format(nn_out_dict):
    class_id = nn_out_dict['class_id']
    front_message = {
                "defect_type":CLASS_NAMES[class_id],
                "message":NAMES_TRANSLATION[class_id],
                "color": colors[class_id]
    }
    return front_message