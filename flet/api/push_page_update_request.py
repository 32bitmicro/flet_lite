from ..utils.get_control_data import get_control_props
from ..utils.appbar_coder import appbar_to_dict
from ..utils.page_posible_props import all_page_posible_props
from ..tools.edit_control_props import edit_control_props
from ..utils.view_coder import view_to_dict
from ..utils.control_coder import control_to_dict
import jsonpickle, json, flet


def push_page_update_request (page_class):
    """Request to remove a control"""
    push_data = {
        "ok" : True,
        "action" : "page_update",
        "props" : {},
        "appbar" : None,
        "views" : [],
        "overlay" : []
    }

    edit_control_props(control=page_class)
    
    for p in all_page_posible_props:
        if hasattr(page_class, p):
            push_data['props'][p] = getattr(page_class, p)

    push_data['props'] = json.loads(jsonpickle.encode(push_data['props']))

    # change the type of some
    for i in page_class.__dict__:
        if page_class.__dict__[i] == flet.MainAxisAlignment.CENTER:
            page_class.__dict__[i] = "center"

    if page_class.appbar != None:
        push_data['appbar'] = appbar_to_dict(page_class.appbar)
    
    for v in page_class.views:
        push_data["views"].append(view_to_dict(view=v))
    
    for olc in page_class.overlay:
        push_data['overlay'].append (control_to_dict(control=olc, overlay=True))

    page_class.api_host.add_update_on_wait (push_data)