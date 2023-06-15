from flet import Page
import flet
import time
import json

# locals
from flet_browser.tools.get_host_update import get_host_updates
from flet_browser.tools.initialise_page_target import run_page_target

class Main:
    def __init__(self, page:flet.Page) -> None:
        self.page = page
        page.update()

        # Initialise that target function on page on real-python
        run_page_target()

        # get updates from the host on real-time.
        while True:
            try:
                self.get_events_and_update()
            except Exception as e:
                print(e)
            time.sleep(0.2)

    def get_events_and_update(self):
        update_content = json.loads(get_host_updates())
        print(update_content)

        if update_content == {}: return

        if update_content["action"] == "add":
            control_data = update_content["control_data"]
            control_name = control_data['name']
            flet_class_dict = control_data['flet_class_dict']
            control = flet.__dict__[f'{control_name}']()
            
            for i in flet_class_dict:
                if hasattr(control, i):
                    setattr(control, i, flet_class_dict[i])

            self.page.add(control)
            control.update()
        
        self.page.update()




async def main (page:Page):
    await page.update_async()

    run_page_target()

    while True:
        



flet.app(target=main)