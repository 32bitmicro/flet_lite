from flet_core_custom import Page
import flet
import json
import asyncio

# locals
from flet_browser.tools.get_host_update import get_host_updates
from flet_browser.tools.initialise_page_target import run_page_target
from flet_browser.flet_utils.generate_control import generate_a_control
from flet_browser.flet_utils.update_page import update_page
from flet_browser.ui.push_error import show_error_content
from flet_browser.flet_utils.update_control import update_a_control
from api.value_update import update_value


class Main:
    def __init__(self, page:flet.Page) -> None:
        self.page = page
        page.main_class = self
        page.update()

        # Initialise that target function on page on real-python
        run_page_target()

        # make a Unique number for each control and save them
        self.all_controls = {}

        # app props
        self.there_is_error = False

        # get updates from the host on real-time.
        # asyncio.run(self.loop_updates_checker())
        self.loop_updates_checker()
        
    def loop_updates_checker (self):
        while True:
            try:
                self.get_events_and_update()
            except Exception as e:
                show_error_content(self.page, error=f"Browser error: {e}")
                print(e)

    def get_events_and_update(self):
        update_content = json.loads(get_host_updates())

        if self.there_is_error: return
        if update_content == {}: return

        # add request
        if update_content["action"] == "add":
            new_control = generate_a_control(self.page, update_content=update_content)
            control_number = update_content["control_data"]['number']
            self.page.add(new_control)
            self.all_controls.update({f"{control_number}":new_control})
            new_control.flet_lite_number = control_number
            new_control.update()
        # error request
        elif update_content['action'] == "error":
            show_error_content(self.page, error=update_content['content'])
            self.there_is_error = True
        # page_update request
        elif update_content["action"] == "page_update":
            update_page(self.page, update_content=update_content)
            self.page.update()
        # update control request
        elif update_content['action'] == "update":
            control_number = update_content['control_data']['control_number']
            if str(control_number) in self.all_controls:
                control_object = self.all_controls[str(control_number)]
                control_updated_props = update_content['control_data']['flet_class_dict']
                update_a_control(control_class=control_object, update_event_dict=control_updated_props)
                control_object.update()

        
        self.page.update()


flet.app(target=Main)