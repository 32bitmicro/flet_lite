from .run_event_function import run_event_function
import json


def update_page (page_class, event_name, data):
    """Update the page props based on the events"""
    if event_name == "resize":
        width, height = str(data).split(",")
        width = float(width)
        height = float(height)
        page_class.width = width
        page_class.window_width = width
        page_class.height = height
        page_class.window_height = height
        
        run_event_function(page_class, page_class, data, "on_resize")
    
    elif event_name == "keyboard_event":
        data_dict = json.loads(data)
        run_event_function(page_class, page_class, data, "on_keyboard_event", append_keys={
            "key":data_dict['key'],
            "shift":data_dict['shift'],
            "ctrl":data_dict['ctrl'],
            "alt":data_dict['alt'],
            "meta" : data_dict['meta']
        })
    
    elif event_name == "route_change":
        route = str(data)
        page_class.route = route

        run_event_function(page_class, page_class, data, "on_route_change")