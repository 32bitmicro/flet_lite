from .run_event_function import run_event_function
import json



def control_update_on_new_event (control, page, event_name, event_data):
    if event_name == "on_change":
        new_value = str(event_data)
        setattr(control, "value", new_value)
        run_event_function(control, page_class=page, event_data=event_data, event_function_name=event_name)
    
    elif event_name == "on_duration_changed":
        new_duration = int(event_data)
        setattr(control, "duration", new_duration)
        run_event_function(control, page_class=page, event_data=event_data, event_function_name=event_name)
    
    elif event_name == "on_position_changed":
        new_position = int(event_data)
        setattr(control, "position", new_position)
        run_event_function(control, page_class=page, event_data=event_data, event_function_name=event_name)

    elif event_name == "on_result":
        evd = json.loads(event_data)
        path = evd['path']
        files = evd['files']
        run_event_function(control, page_class=page, event_data=event_data,
                        event_function_name=event_name, append_keys={"path":path, "files":files, "name":"result"})

    
    else:
        run_event_function(control, page_class=page, event_data=event_data, event_function_name=event_name)