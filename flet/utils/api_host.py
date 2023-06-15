from flask import Flask
from flask_cors import CORS

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

        @app.route("/", methods=["POST"])
        def index():
            self.page.start_target()
            return {}


        @app.route("/get_data", methods=["POST"])
        def get_data ():
            if len(self.updates_and_events) != 0:
                d = self.updates_and_events[-1]
                self.updates_and_events.remove(d)
                return d
            return {}


        @app.route("/push_data", methods=["POST"])
        def push_data():
            return {}

        app.run(port=self.port)
    
    def add_update_on_wait(self, update):
        pass