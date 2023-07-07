from api.get_host_updates import get_host_updates
from api.initialize_page_target import initialize_page_target
from tools.manage_host_updates import manage_host_updates
from flet_utils.manage_page_events import manage_page_events
import flet
import time
import traceback
import asyncio
import json, os

from api.push_event_to_host import push_event_to_host

class Main:
    def __init__(self, page:flet.Page) -> None:
        self.page = page
        page.update()

        # props
        self.all_controls = {}
        self.parents_of_controls = {}
        self.facing_error = False

        time.sleep(0.1)
        # asyncio.run(self.check_for_host_updates())
        asyncio.create_task(self.check_for_host_updates())
    
    async def check_for_host_updates (self):
        try: initialize_page_target_result = initialize_page_target(width=self.page.width, height=self.page.height)
        except: self.push_error_page("Browser error: Cant connect with the host"); return;
        
        if initialize_page_target_result['ok'] == False:
            self.push_error_page(f"Host error: {initialize_page_target_result['error']}")
            return
        
        # manage page events
        manage_page_events(main_class=self, page=self.page) #! This is not working..
        
        self.page.update()
        
        while self.facing_error == False:
            try: 
                u = get_host_updates(main_class=self)
                if u == {}: pass
                else:
                    for upd in u['updates']:
                        manage_host_updates(update_dict=upd, main_class=self)
            except Exception as e:
                traceback.print_exc()
                self.push_error_page(f"{e}")
            # time.sleep(0.05)
            await asyncio.sleep(0.05)
        
        print("This page is no longer updated.")
    
    def push_error_page (self, error:str):
        if self.facing_error: return
        self.page.clean()
        self.page.appbar = None
        self.page.bgcolor = flet.colors.WHITE
        self.facing_error = True
        self.page.vertical_alignment = flet.MainAxisAlignment.CENTER
        self.page.controls.append(flet.Column([
            flet.Row([
                flet.Icon(name=flet.icons.INFO_OUTLINED, color="red")
            ], alignment=flet.MainAxisAlignment.CENTER),
            flet.Row([
                flet.Text(f"{error}", color="red", text_align=flet.TextAlign.CENTER)
            ], alignment=flet.MainAxisAlignment.CENTER)
        ], alignment=flet.MainAxisAlignment.CENTER))
        self.page.update()
    
    def push_to_host (self, event_name:str, flet_class_number:int, event_data:dict):
        """Push event to the host"""
        if self.facing_error: return
        print("Debug: The function `push_to_host` is called!")
        try: push_event_to_host(event_name, flet_class_number, event_data)
        except Exception as e: self.push_error_page(f"Browser error: {e}")


if os.path.isfile("app_data.json"):
    app_data = json.loads(open("app_data.json", encoding="utf-8").read())
    assets_dir = app_data['assets_dir']
    flet.app(target=Main, assets_dir=f"{assets_dir}")
else:
    flet.app(target=Main)