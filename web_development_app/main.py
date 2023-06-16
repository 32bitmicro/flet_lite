from flet import Page
import flet
import time
import json
import asyncio

# locals
from flet_browser.tools.get_host_update import get_host_updates
from flet_browser.tools.initialise_page_target import run_page_target
from flet_browser.flet_utils.generate_control import generate_a_control

class Main:
    def __init__(self, page:flet.Page) -> None:
        self.page = page
        page.update()

        # Initialise that target function on page on real-python
        run_page_target()

        # get updates from the host on real-time.
        asyncio.run(self.loop_updates_checker())
    
    async def loop_updates_checker (self):
        while True:
            try:
                self.get_events_and_update()
            except Exception as e:
                print(e)

    def get_events_and_update(self):
        update_content = json.loads(get_host_updates())

        if update_content == {}: return

        if update_content["action"] == "add":
            new_control = generate_a_control(self.page, update_content=update_content)
            self.page.add(new_control)
            new_control.update()
        
        self.page.update()


flet.app(target=Main)