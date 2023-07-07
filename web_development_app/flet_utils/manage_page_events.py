import json, flet



def manage_page_events (main_class, page:flet.Page):
    def on_page_event (e):
        event_info = e.__dict__
        main_class.push_to_host(event_info['name'], "PAGE", event_info['data'])
    
    page.on_resize = on_page_event
    page.on_scroll = on_page_event
    page.on_route_change = on_page_event
    page.on_keyboard_event = on_page_event
    page.update()