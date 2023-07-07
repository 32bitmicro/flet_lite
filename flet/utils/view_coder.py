from .control_coder import control_to_dict, dict_to_control
from .appbar_coder import appbar_to_dict, dict_to_appbar
import json, jsonpickle
import flet



def view_to_dict (view:flet.View) -> dict:
    
    route = view.route

    if view.floating_action_button == None:
        floating_action_button = None
    else:
        floating_action_button = control_to_dict(view.floating_action_button, no_control_number=True)
    
    all_view_controls = []
    for c in view.controls:
        all_view_controls.append(control_to_dict(c))
    

    if view.horizontal_alignment == None:
        horizontal_alignment = None
    else:
        horizontal_alignment = str(view.horizontal_alignment)
    
    if view.vertical_alignment == None:
        vertical_alignment = None
    else:
        vertical_alignment = str(view.vertical_alignment)
    

    if view.appbar == None:
        appbar_data = None
    else:
        appbar_data = appbar_to_dict(appbar=view.appbar)
    
    if view.spacing == None:
        spacing = None
    else:
        spacing = float(view.spacing)
    
    if view.padding == None:
        padding = None
    else:
        padding = view.padding


    view_dict = {
        "route" : route,
        "floating_action_button" : floating_action_button,
        "controls" : all_view_controls,
        "scroll" : str(view.scroll),
        "spacing" : spacing,
        "horizontal_alignment" : horizontal_alignment,
        "padding" : padding,
        "vertical_alignment" : vertical_alignment,
        "appbar" : appbar_data
    }

    return view_dict

def dict_to_view (view_dict:dict) -> flet.View:
    view_class = flet.View()

    if view_dict['appbar'] != None:
        view_class.appbar = dict_to_appbar(view_dict['appbar'])

    for c in view_dict['controls']:
        view_class.controls.append(dict_to_control(control_dict=c))
    
    if view_dict['floating_action_button'] != None:
        view_class.floating_action_button = dict_to_control(view_dict['floating_action_button'], no_control_number=True)

    view_class.scroll = view_dict['scroll']
    view_class.spacing = view_dict['spacing']
    view_class.padding = view_dict['padding']
    view_class.vertical_alignment = view_dict['vertical_alignment']
    view_class.horizontal_alignment = view_dict['horizontal_alignment']

    return view_class