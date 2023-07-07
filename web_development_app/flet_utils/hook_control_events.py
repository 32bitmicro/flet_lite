import flet

all_actions = [
    "on_change", "on_submit", "on_focus", "on_blur", "on_hover", "on_click"
]


class HookControlEvents:
    """
    This will search for all control events to hook them into a function.
    
    For example if a control have a prop called `on_change`, it will hook it to push it to host on per call.
    """
    def __init__(self, control:flet.Control, main_class) -> None:
        self.control = control
        self.main_class = main_class

        self.search_for_event_props()

    def search_for_event_props (self):
        for action_prop in all_actions:
            if hasattr(self.control, action_prop):
                self.event_hook(action_prop)
    
    def event_hook (self, event_name:str):
        def call_this_function (e):
            event_info = e.__dict__
            self.main_class.push_to_host(f"{event_name}", self.control.flet_lite_number, event_info['data'])
        
        setattr(self.control, event_name, call_this_function)