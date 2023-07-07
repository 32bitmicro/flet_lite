import flet

from .hook_control_events import HookControlEvents


def generate_flet_control (control_dict:dict, main_class) -> flet.Control:
    control_name = control_dict['name']
    control_number = control_dict['number']
    control_flet_class_dict = control_dict['flet_class_dict']

    control = flet.__dict__[f'{control_name}']()
    setattr(control, "flet_lite_number", control_number)

    HookControlEvents(control=control, main_class=main_class)

    for prop in control_flet_class_dict:
        if hasattr(control, prop):
            setattr(control, prop, control_flet_class_dict[prop])
    
    return control