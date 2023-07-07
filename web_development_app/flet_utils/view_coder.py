from .control_coder import dict_to_control
from .appbar_coder import dict_to_appbar
from .hook_control_events import HookControlEvents
import flet


def dict_to_view (view_dict:dict, main_class) -> flet.View:
    view_class = flet.View()

    if view_dict['appbar'] != None:
        view_class.appbar = dict_to_appbar(view_dict['appbar'])

    for c in view_dict['controls']:
        view_class.controls.append(dict_to_control(control_dict=c))
        HookControlEvents(c, main_class=main_class)
    
    if view_dict['floating_action_button'] != None:
        view_class.floating_action_button = dict_to_control(view_dict['floating_action_button'], no_control_number=True)

    view_class.scroll = view_dict['scroll']
    view_class.spacing = view_dict['spacing']
    view_class.padding = view_dict['padding']
    view_class.vertical_alignment = view_dict['vertical_alignment']
    view_class.horizontal_alignment = view_dict['horizontal_alignment']

    return view_class