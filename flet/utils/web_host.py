from typing import Any
from .get_free_port import free_port
import http.server
import socketserver


class MyHandler(http.server.SimpleHTTPRequestHandler):
	def log_message(self, format, *args):
		pass

class WebFilesHost:
    """Host the files of the `web` folder that uses flutter.js and pyodide to show the UI on browser"""
    def __init__ (self):
        self.port = free_port()
        self.url = f"http://localhost:{self.port}"
        self.web_url = f"{self.url}/web/"
    
    def start (self):
        """start the server"""
        PORT = self.port

        with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
            httpd.serve_forever()