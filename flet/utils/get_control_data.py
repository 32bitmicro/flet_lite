import flet, typing

from typing import Literal
try:
    from .all_props_posible import all_posible_props
except:
    from all_props_posible import all_posible_props

def get_control_props (control:flet.Control):
    wanted_props = {}
    
    for pp in all_posible_props():
        if hasattr(control, pp):
            value = getattr(control, pp)
            if typing.get_origin(value) is typing.Literal:
                if hasattr(value, "name"):
                    value = value.name
                else:
                    value = str(value)
            wanted_props[pp] = value
    
    return wanted_props