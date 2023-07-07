from tools.post_request import http_POST_request
import json



def push_event_to_host (event_name:str, flet_class_number:int, data:str):
    url_of_host = open("localhost_api_url.txt", encoding="utf-8").read()

    r = http_POST_request(f"{url_of_host}/push_data", post_data={
        "event_name" : event_name,
        "flet_class_number" : flet_class_number,
        "data" : data
    })

    return json.loads(r)