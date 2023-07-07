import json, jsonpickle, flet
try:
    from .get_control_data import get_control_props
except:
    from get_control_data import get_control_props




def control_to_dict (control, overlay=False, no_control_number=False, with_childs=True) -> dict:
    d = {
        "name" : str(type(control).__name__),
        "flet_class_dict" : json.loads(jsonpickle.encode(get_control_props(control=control))),
        "overlay" : overlay
    }

    if no_control_number == False:
        d['number'] = int(control.flet_lite_number)
        d['parent'] = control.parent
    

    if with_childs:
        if hasattr(control, "controls"):
            d['controls'] = []
            for c in control.controls:
                d['controls'].append(control_to_dict(c, no_control_number=no_control_number))
        
        if hasattr(control, "content"):
            if control.content != None:
                d['content'] = control_to_dict(control=control.content, no_control_number=no_control_number)
            else:
                d['content'] = None

    return d



def dict_to_control (control_dict:dict, no_control_number=False) -> flet.Control:
    control_name = control_dict['name']

    control = flet.__dict__[f"{control_name}"]()
    if no_control_number == False:
        setattr(control, "flet_lite_number", control_dict['number'])
        control.parent = control_dict['parent']

    for i in control_dict['flet_class_dict']:
        if hasattr(control, i):
            setattr(control, i, control_dict['flet_class_dict'][i])
    

    if "controls" in control_dict:
        for c in control_dict['controls']:
            control.controls.append(dict_to_control(c, no_control_number=True))
    
    if "content" in control_dict:
        if control_dict['content'] != None:
            control.content = dict_to_control(control_dict['content'], no_control_number=True)

    return control


