from flet_core.control import Control



def update_a_control (control_class:Control, update_event_dict:dict):
    for i in update_event_dict:
        if hasattr(control_class, i):
            setattr(control_class, i, update_event_dict[i])