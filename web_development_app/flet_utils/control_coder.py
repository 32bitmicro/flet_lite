import flet



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
