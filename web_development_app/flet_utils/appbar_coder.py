from .control_coder import dict_to_control
import flet

    

def dict_to_appbar (appbar_dict:dict):
    appbar_class = flet.AppBar()

    if appbar_dict['actions'] == None: appbar_dict['actions'] = []
    for con in appbar_dict['actions']:
        appbar_class.actions.append(dict_to_control(con, no_control_number=True))
    

    if appbar_dict['automatically_imply_leading'] != None:
        appbar_class.automatically_imply_leading = appbar_dict['automatically_imply_leading']
    
    appbar_class.bgcolor = appbar_dict['bgcolor']
    appbar_class.center_title = appbar_dict['center_title']
    appbar_class.color = appbar_dict['color']

    if appbar_dict['leading'] == None:
        appbar_class.leading = None
    else:
        appbar_class.leading = dict_to_control(appbar_dict['leading'], no_control_number=True)
    
    appbar_class.leading_width = appbar_dict['leading_width']

    if appbar_dict['title'] == None:
        appbar_class.title = None
    else:
        appbar_class.title = dict_to_control(appbar_dict['title'], no_control_number=True)
    
    appbar_class.toolbar_height = appbar_dict['toolbar_height']

    return appbar_class