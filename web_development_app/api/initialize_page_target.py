from tools.post_request import http_POST_request
from flet_utils.view_coder import dict_to_view
import json, flet


def initialize_page_target (width, height):
    url_of_host = open("localhost_api_url.txt", encoding="utf-8").read()

    updates = http_POST_request(url=url_of_host, post_data={"width":width, "height":height})

    return json.loads(updates)