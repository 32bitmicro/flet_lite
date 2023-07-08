from flask import Flask, request
from flask_cors import CORS
import threading, json, os
from .get_free_port import free_port
from ..api.manage_client_pushes import manage_client_pushes


class ApiHost:
    """Host the API that used for communication between pyodide and real python."""
    def __init__ (self, page):
        self.name = "__main__"
        self.page = page

        self.updates_and_events = []

        self.port = free_port()
        self.app = Flask(self.name)
        CORS(self.app)
        
        self.url = f"http://127.0.0.1:{self.port}"

    def host (self):
        app = self.app

        import logging
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)
        app.logger.disabled = True
        log.disabled = True

        @app.route("/", methods=["POST"])
        def index():
            json_data = json.loads(str(request.data.decode()))
            self.page.width = json_data['width']
            self.page.height = json_data['height']
            self.page.window_width = self.page.width
            self.page.window_height = self.page.height
            threading.Thread(target=self.page.start_target, daemon=True).start()
            return {"ok":True}


        @app.route("/get_data", methods=["POST"])
        def get_data ():
            if len(self.updates_and_events) != 0:
                updates_dict = {
                    "ok" : True,
                    "updates" : self.updates_and_events
                }
                self.updates_and_events = []
                return updates_dict
            return {}


        @app.route("/push_data", methods=["POST"])
        def push_data():
            json_data = json.loads(str(request.data.decode()))
            # print(f"{json_data}")
            manage_client_pushes(push_dict=json_data, page_class=self.page)
            return {}
        
        @app.route("/close", methods=["GET"])
        def close_program ():
            os._exit(1)
            return {}

        print(f"To close the program, open this on terminal: '{self.url}/close'")
        app.run(port=self.port)
    
    def add_update_on_wait(self, update:dict):
        self.updates_and_events.append(update)
    
    def push_an_error(self, error:str):
        self.updates_and_events.append({
            "action" : "error",
            "content" : str(error)
        })