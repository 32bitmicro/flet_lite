from flask import Flask, request
from flask_cors import CORS
import threading
from .get_free_port import free_port


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
            threading.Thread(target=self.page.start_target, daemon=True).start()
            return {}


        @app.route("/get_data", methods=["POST"])
        def get_data ():
            if len(self.updates_and_events) != 0:
                d = self.updates_and_events[0]
                self.updates_and_events.remove(d)
                return d
            return {}


        @app.route("/push_data", methods=["POST"])
        def push_data():
            print(request.values)
            return {}

        app.run(port=self.port)
    
    def add_update_on_wait(self, update:dict):
        self.updates_and_events.append(update)
    
    def push_an_error(self, error:str):
        self.updates_and_events.append({
            "action" : "error",
            "content" : str(error)
        })