from ..utils.get_control_data import get_control_props
import jsonpickle, json


def push_update_request (controls, page_class):
    push_data = {
        "ok" : True,
        "action" : "update",
        "controls" : []
    }
    

    for con in controls:
        push_data["controls"].append({
            "number" : int(con.flet_lite_number),
            "flet_class_dict" : json.loads(jsonpickle.encode(get_control_props(control=con)))
        })

    page_class.api_host.add_update_on_wait (push_data)