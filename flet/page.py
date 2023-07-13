from typing import Any
from .utils.api_host import ApiHost
from .utils.web_host import WebFilesHost
from .tools.setup_web import WebDirSet
from .api.push_add_request import push_add_request
from .api.push_update_request import push_update_request
from .api.push_remove_request import push_remove_request
from .api.push_page_update_request import push_page_update_request
from .api.push_clean_request import push_clean_request
from .api.push_go_route_request import push_go_route_request
from .utils.page_posible_props import all_page_posible_props
from .utils.get_all_subcontrols import get_all_subControls_on_the_page
from .tools.platform_specifics.get_platform_name import get_platform_name
from .tools.platform_specifics.pythonista_webview import safari_in_app_view
import threading
import webbrowser
import time, asyncio, traceback
import flet


class Page (object):
    def __init__ (self, target_function, assets_dir_path:str):
        self.target_function = target_function

        # set all hosts without starting them.
        self.api_host = ApiHost(page=self)
        self.web_files_host = WebFilesHost()
        
        # Set the development web directory
        WebDirSet(localhost_api_url=self.api_host.url, assets_dir_path=assets_dir_path)

        # Start the host API
        threading.Thread(target=self.api_host.host, daemon=True).start()

        # start the web development dir for browser
        threading.Thread(target=self.web_files_host.start, daemon=True).start()

        time.sleep(1)

        # start opening the localhost URL in the browser, or platform specific view.
        print(self.web_files_host.web_url) #? print the URL of the app
        if get_platform_name() == "pythonista":
            safari_in_app_view(str(self.web_files_host.web_url))
        else:
            webbrowser.open(self.web_files_host.web_url)

        # set all page props
        for i in all_page_posible_props:
            setattr(self, i, None)
        
        # page class's flet props
        self.appbar = None
        self.route = "/"
        self.last_control_number = 0
        self.__controls_are_pushed = [] # The controls that did be on the page at least once.
        self.views = []
        self.overlay = []
        self.controls = []
        self.controls_dict_numbers = {}
    
    def start_target (self):
        """When the host and client browser are ready, this is will be called to start the target function."""
        print("Connected to a browser..")
        try:
            self.target_function(self)
        except Exception as e:
            self.api_host.push_an_error(error=str(e))
            traceback.print_exc()
    

    #! ---------Flet page functions----------


    def add(self, control, parent="page"):
        if hasattr(control, "build"):
            control.page = self
            control.parent = parent
            control.flet_lite_number = self.last_control_number
            self.last_control_number = self.last_control_number + 1
            self.controls_dict_numbers[f'{control.flet_lite_number}'] = control
            self.__controls_are_pushed.append(control)
            control = control.build()
        
        control.is_overlay = False
        control.flet_lite_number = self.last_control_number
        control.parent = parent
        control.page = self

        push_add_request(controls=[control], page_class=self)
        if control not in self.__controls_are_pushed:
            self.__controls_are_pushed.append(control)
        
        if parent == "page" and control not in self.controls:
            self.controls.append(control)
        
        self.controls_dict_numbers[f"{control.flet_lite_number}"] = control

        self.last_control_number = self.last_control_number + 1

        if hasattr (control, "controls"):
            for I in control.controls:
                self.add(I, parent=control.flet_lite_number)
        elif hasattr(control, "content"):
            if control.content != None:
                self.add(control=control.content, parent=control.flet_lite_number)    

    def setup_overlay_control (self, c:flet.Control):
        c.flet_lite_number = self.last_control_number
        self.last_control_number = self.last_control_number + 1

        c.page = self
        c.is_overlay = True
        c.parent = "page"

        self.controls_dict_numbers[f"{c.flet_lite_number}"] = c

        return c

    
    def update (self, *controls):
        # push the controls that are not pushed yet
        for con in self.controls:
            if con not in self.__controls_are_pushed:
                self.add(con)
        
        for sub_con in get_all_subControls_on_the_page(parent=self):
            if sub_con not in self.__controls_are_pushed:
                if hasattr(sub_con, "parent"):
                    self.add(sub_con, parent=sub_con.parent.flet_lite_number)
                else:
                    self.add(sub_con)
        
        # push controls that are overlay and still not pushed
        for overlay_control in self.overlay:
            self.setup_overlay_control(c=overlay_control)
        
        # update sub controls
        all_controls_to_update = []
        for control in controls:
            all_controls_to_update.append(control)
            for i in get_all_subControls_on_the_page(control):
                if i.page != None: i.page = self
                all_controls_to_update.append(i)
        

        # give view's controls a number
        for v in self.views:
            v.flet_lite_number = -1
            for i in get_all_subControls_on_the_page(parent=v):
                if not hasattr(i, "flet_lite_number"):
                    setattr(i, "flet_lite_number", self.last_control_number)
                
                if i in self.__controls_are_pushed: pass
                else:
                    self.__controls_are_pushed.append(i)

                self.controls_dict_numbers[f"{i.flet_lite_number}"] = i
                self.last_control_number = self.last_control_number + 1
        

        # update page props
        push_page_update_request(self)


        if controls == ():
            for i in get_all_subControls_on_the_page(parent=self):
                all_controls_to_update.append(i)

        push_update_request(controls=all_controls_to_update, page_class=self)

        # remove the controls that removed
        all_controls = get_all_subControls_on_the_page(self)
        for con in self.__controls_are_pushed:
            if con not in all_controls:
                push_remove_request(control_number=con.flet_lite_number, page_class=self)
    

    def remove (self, control):
        if control in self.controls:
            self.controls.remove(control)
        else:
            raise ValueError("list.remove(x): x not in list")
        
        self.update()
    


    def clean (self, control=None):
        if control == None:
            push_clean_request("page", page_class=self)
            for i in self.controls:
                if i in list(self.__controls_are_pushed):
                    self.__controls_are_pushed.remove(i)
            self.controls.clear()
        else:
            push_clean_request(control.flet_lite_number, page_class=self)
            for i in control.controls:
                if i in list(self.__controls_are_pushed):
                    self.__controls_are_pushed.remove(i)
            control.controls.clear()
    
    def _clean (self, control):
        self.clean(control)
    

    def go (self, route):
        push_go_route_request(route_name=route, page_class=self)


    def window_center(self): pass

    @property
    def get_all_pushed_controls (self):
        return self.__controls_are_pushed