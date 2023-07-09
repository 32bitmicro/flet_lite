from typing import Literal
from .page import Page
import signal, sys


WEB_BROWSER = "web_browser"
FLET_APP = "flet_app"
FLET_APP_WEB = "flet_app_web"
FLET_APP_HIDDEN = "flet_app_hidden"

AppViewer = Literal[None, "web_browser", "flet_app", "flet_app_web", "flet_app_hidden"]

WebRenderer = Literal[None, "auto", "html", "canvaskit"]


def app (
    target,
    name="",
    host=None,
    port=0,
    view: AppViewer = FLET_APP,
    assets_dir=None,
    upload_dir=None,
    web_renderer="canvaskit",
    use_color_emoji=False,
    route_url_strategy="path",
    auth_token=None
    ):
    if view != FLET_APP:
        print("WARNING: flet-lite will always work on web_browser view mode.")
    
    Page(target_function=target, assets_dir_path=assets_dir)

    # Define a signal handler function
    def signal_handler(signal, frame):
        sys.exit()

    # Set the signal handler for SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)

    # open a loop so the threads of the two hosts not closed.
    still_open = True
    while still_open:
        pass