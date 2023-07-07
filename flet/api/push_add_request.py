from ..utils.get_control_data import get_control_props
from ..utils.control_coder import control_to_dict
import jsonpickle, json


def push_add_request (controls, page_class):
    push_data = {
        "ok" : True,
        "action" : "add",
        "controls" : []
    }
    

    for con in controls:
        push_data["controls"].append(control_to_dict(control=con, with_childs=False))

    page_class.api_host.add_update_on_wait (push_data)