from flet_core.event import Event
from flet_core.event_handler import EventHandler
import threading



def run_event_function (control, page_class, event_data, event_function_name, append_keys=None):
    def do_event_function ():
        function_ = getattr(control, event_function_name)
        if isinstance(function_, EventHandler):
            function_ = function_.__dict__['_EventHandler__handlers']
            function_ = next(iter(function_))
            threading.Thread(target=function_, args=[e], daemon=True).start()
        else:
            threading.Thread(target=function_, args=[e], daemon=True).start()
    # ----
    if hasattr(control, event_function_name):
        e = Event(target="", name=f"{event_function_name}", data=event_data)
        e.control = control
        e.page = page_class
        if getattr(control, event_function_name) != None:
            if append_keys != None:
                for k in append_keys:
                    setattr(e, k, append_keys[k])
            if not hasattr(getattr(control, event_function_name), "__dict__"):
                do_event_function()
            elif getattr(control, event_function_name).__dict__ == {}:
                do_event_function()
            elif getattr(control, event_function_name).__dict__['_EventHandler__handlers'] != {}:
                do_event_function()