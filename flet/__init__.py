from typing import Literal
from flet_core import *

from .flet import app

FLET_APP = "flet_app"
WEB_BROWSER = "web_browser"
AppViewer = Literal[None, "web_browser", "flet_app", "flet_app_web", "flet_app_hidden"]

WebRenderer = Literal[None, "auto", "html", "canvaskit"]