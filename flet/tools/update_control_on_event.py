from .run_event_function import run_event_function




def control_update_on_new_event (control, page, event_name, event_data):
    if event_name == "on_change":
        new_value = str(event_data)
        setattr(control, "value", new_value)
        run_event_function(control, page_class=page, event_data=event_data, event_function_name=event_name)
    elif event_name == "on_click" or event_name == "on_hover":
        run_event_function(control, page_class=page, event_data=event_data, event_function_name=event_name)