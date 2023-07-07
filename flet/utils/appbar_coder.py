try:
    from .get_control_data import get_control_props
    from .control_coder import control_to_dict, dict_to_control
except:
    from get_control_data import get_control_props
    from control_coder import control_to_dict, dict_to_control
import flet



def appbar_to_dict (appbar:flet.AppBar):
    action_controls = []
    # get appbar actions
    if appbar.actions != None:
        for con in appbar.actions:
            action_controls.append(control_to_dict(control=con, no_control_number=True))
    
    automatically_imply_leading = appbar.automatically_imply_leading
    bgcolor = appbar.bgcolor
    center_title = appbar.center_title
    color = appbar.color
    if appbar.leading == None:
        leading_control = None
    else:
        leading_control = control_to_dict(appbar.leading, no_control_number=True)
    
    leading_width = appbar.leading_width
    if appbar.title == None:
        title = appbar.title
    else:
        title = control_to_dict(appbar.title, no_control_number=True)
    toolbar_height = appbar.toolbar_height

    appbar_dict = {
        "actions" : action_controls,
        "automatically_imply_leading" : automatically_imply_leading,
        "bgcolor" : bgcolor,
        "center_title" : center_title,
        "color" : color,
        "leading" : leading_control,
        "leading_width" : leading_width,
        "title" : title,
        "toolbar_height" : toolbar_height
    }
    return appbar_dict

    

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

if __name__ == "__main__":
    def test(page:flet.Page):
        apc = appbar_to_dict(flet.AppBar(bgcolor="red", title=flet.Text("I am a title!"), actions=[
            flet.TextButton(content=flet.Text("Me just action"))
        ]))

        page.add(dict_to_appbar(apc))
        
    flet.app(target=test)