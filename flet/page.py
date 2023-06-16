from .utils.api_host import ApiHost
from .utils.web_host import WebFilesHost
from .tools.setup_web import WebDirSet
from .utils.all_props_posible import all_posible_props
import threading
import webbrowser
import time, json


class Page (object):
    def __init__ (self, target_function, debug):
        self.target_function = target_function

        # set all hosts without starting them.
        self.api_host = ApiHost(page=self)
        self.web_files_host = WebFilesHost()
        
        # Set the development web directory
        WebDirSet(localhost_api_url=self.api_host.url)

        # Start the host API
        threading.Thread(target=self.api_host.host, daemon=True).start()

        # start the web development dir for browser
        threading.Thread(target=self.web_files_host.start, daemon=True).start()

        time.sleep(1)
        if debug == False:
            webbrowser.open(self.web_files_host.web_url)
        else:
            open("localhost_api_url.txt", "w+", encoding="utf-8").write(self.api_host.url)

    
    def start_target (self):
        """When the host and client browser are ready, this is will be called to start the target function."""
        print("Connected with a browser..")
        self.target_function(self)
    
    def add(self, *controls):
        for control in controls:
            wanted_props = {}
            for p in all_posible_props():
                if hasattr(control, p):
                    value_of_attr = getattr(control, p)
                    wanted_props.update({f"{p}":value_of_attr})
            self.api_host.add_update_on_wait(
                {
                    "action" : "add",
                    "control_data" : {
                        "name" : str(type(control).__name__),
                        "flet_class_dict" : wanted_props
                    }
                }
            )