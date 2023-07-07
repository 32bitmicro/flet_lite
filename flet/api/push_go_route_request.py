from ..utils.get_control_data import get_control_props
import jsonpickle, json


def push_go_route_request (route_name:str, page_class):
    push_data = {
        "ok" : True,
        "action" : "go_route",
        "route_name" : route_name
    }
    

    page_class.api_host.add_update_on_wait (push_data)