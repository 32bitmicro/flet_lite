from tools.post_request import http_POST_request
import json, traceback


def get_host_updates (main_class):
    url_of_host = open("localhost_api_url.txt", encoding="utf-8").read()

    try:
        updates = http_POST_request(url=f"{url_of_host}/get_data", post_data={})
        return json.loads(updates)
    except Exception as e:
        traceback.print_exc()
        main_class.push_error_page("Browser error: Cant connect with the host to get updates.")
        return