from flet_core.control import Control
from ..utils.all_props_posible import all_posible_props


def control_dict_object (control:Control):
    wanted_props = {}
    for p in all_posible_props():
        if hasattr(control, p):
            value_of_attr = getattr(control, p)
            wanted_props.update({f"{p}":value_of_attr})
    

    event_dict = {
        "name" : str(type(control).__name__),
        "number" : control.flet_lite_control_number,
        "flet_class_dict" : wanted_props
    }

    return event_dict