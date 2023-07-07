from api.manage_add_request import manage_add_request
from api.manage_update_request import manage_update_request
from api.manage_clean_request import manage_clean_request
from api.manage_remove_request import manage_remove_request
from api.manage_page_update_request import manage_page_update_request
from api.manage_route_request import manage_route_request


def manage_host_updates (update_dict:dict, main_class):
    if update_dict == {}: return
    if update_dict == None: return
    action_name = update_dict['action']

    if action_name == "add":
        controls = update_dict['controls']
        manage_add_request(controls=controls, main_class=main_class)

    elif action_name == "error":
        main_class.push_error_page(update_dict['content'])

    elif action_name == "page_update":
        manage_page_update_request(update_dict=update_dict, main_class=main_class)
        main_class.page.update()
    
    elif action_name == "update":
        controls = update_dict['controls']
        for c in controls:
            manage_update_request(c['number'], main_class, c['flet_class_dict'])
        main_class.page.update()
    
    elif action_name == "remove":
        control_number = update_dict['control_number']
        manage_remove_request(control_number=control_number, main_class=main_class)

    elif action_name == "clean":
        control_number = update_dict['control_number']
        manage_clean_request(control_number=control_number, main_class=main_class)
    
    elif action_name == "go_route":
        route_name = update_dict['route_name']
        manage_route_request(route_name, main_class=main_class)
