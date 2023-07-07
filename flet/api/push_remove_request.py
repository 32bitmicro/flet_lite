from ..utils.get_control_data import get_control_props
import jsonpickle, json


def push_remove_request (control_number:int, page_class):
    """Request to remove a control"""
    push_data = {
        "ok" : True,
        "action" : "remove",
        "control_number" : control_number
    }

    page_class.api_host.add_update_on_wait (push_data)