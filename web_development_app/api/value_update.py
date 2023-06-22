from flet_browser.tools.http_post_request import http_POST_request



def update_value (control_number, new_value):
    url_of_host = open("localhost_api_url.txt", encoding="utf-8").read()

    content = http_POST_request(url=f"{url_of_host}/push_data", post_data={
        "action" : "push",
        "control_update" : True,
        "control_data" : {
            "number" : control_number,
            "flet_class_dict" : {
                "value" : new_value
            }
        }
    })