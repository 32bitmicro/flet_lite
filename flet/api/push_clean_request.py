from ..utils.get_control_data import get_control_props
import jsonpickle, json


def push_clean_request (control_number, page_class):
    push_data = {
        "ok" : True,
        "action" : "clean",
        "control_number" : f"{control_number}"
    }

    page_class.api_host.add_update_on_wait (push_data)