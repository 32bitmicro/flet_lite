from .utils.api_host import ApiHost
from .utils.web_host import WebFilesHost
from .tools.setup_web import WebDirSet
from .utils.all_props_posible import all_posible_props
from .utils.control_dict_object import control_dict_object
from .api.generate_ctrl_update_dict import generate_control_update_dict
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
            print(self.web_files_host.web_url)
            webbrowser.open(self.web_files_host.web_url)
        else:
            open("localhost_api_url.txt", "w+", encoding="utf-8").write(self.api_host.url)
        
        # page class's flet props
        self.last_control_number = 0
        self.__controls_are_pushed = []
        self.controls = []
        self.controls_dict_numbers = {}

    
    def start_target (self):
        """When the host and client browser are ready, this is will be called to start the target function."""
        print("Connected to a browser..")
        try:
            self.target_function(self)
        except Exception as e:
            self.api_host.push_an_error(error=str(e))
            print(e)
    

    #! ---------Flet page functions----------


    def add(self, *controls):
        for control in controls:
            self.controls.append(control)

            control.page = self
            control.flet_lite_control_number = self.last_control_number

            self.__controls_are_pushed.append(control)
            self.controls_dict_numbers.update({f"{self.last_control_number}":control})

            wanted_props = {}
            for p in all_posible_props():
                if hasattr(control, p):
                    value_of_attr = getattr(control, p)
                    wanted_props.update({f"{p}":value_of_attr})
            self.api_host.add_update_on_wait(
                {
                    "action" : "add",
                    "control_data" : control_dict_object(control=control)
                }
            )
            self.last_control_number = self.last_control_number + 1
    
    def update (self, *controls):
        page_props = {}
        for p in self.__dict__:
            if isinstance(p, int) or isinstance(p, bool) or isinstance(p, str) or isinstance(p, float) or isinstance(p, list) or isinstance(p, tuple):
                if str(p) in ["controls", "_Page__controls_are_pushed", "api_host", 
                              "web_files_host", "target_function", "controls_dict_numbers"]: pass
                else:
                    page_props.update({f"{p}":self.__dict__[p]})
            elif self.__dict__[p] == None: pass
            else:
                pass
        
        # push the controls that are not on the page to be on the page
        for i in self.controls:
            if i not in self.__controls_are_pushed:
                self.add(i)
        

        # update controls if existed
        if controls != ():
            for con in controls:
                control_update_event_data = generate_control_update_dict(control=con)
                self.api_host.add_update_on_wait(update=control_update_event_data)
        else:
            for con in self.controls:
                control_update_event_data = generate_control_update_dict(control=con)
                self.api_host.add_update_on_wait(update=control_update_event_data)

        
        self.api_host.add_update_on_wait(
            {
                "action" : "page_update",
                "props" : page_props,
                "appbar_class_props" : {}
            }
        )