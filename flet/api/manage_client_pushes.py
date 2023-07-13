from ..tools.update_page_info import update_page
from ..tools.update_control_on_event import control_update_on_new_event



def manage_client_pushes(push_dict:dict, page_class):
    event_name = push_dict['event_name']
    control_number = push_dict['flet_class_number']
    event_data = push_dict['data']

    if str(control_number).lower() == "page":
        update_page(page_class=page_class, event_name=event_name, data=event_data)
    else:
        if str(control_number) in page_class.controls_dict_numbers:
            control = page_class.controls_dict_numbers[str(control_number)]
            if control.page == None:
                control.page = page_class
            control_update_on_new_event(control=control, page=page_class, event_name=event_name, event_data=event_data)