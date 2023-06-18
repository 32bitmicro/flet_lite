from flet_core.control import Control
from ..utils.all_props_posible import all_posible_props
from ..utils.control_dict_object import control_dict_object



def generate_control_update_dict (control:Control):
    if not hasattr(control, "flet_lite_control_number"):
        raise Exception("You need to add the control to the page first!")

    wanted_props = {}
    for p in all_posible_props():
        if hasattr(control, p):
            value_of_attr = getattr(control, p)
            wanted_props.update({f"{p}":value_of_attr})
    
    dict_event = {
        "action" : "update",
        "control_data" : {
            "control_number" : control.flet_lite_control_number,
            "flet_class_dict" : wanted_props
        }
    }

    return dict_event