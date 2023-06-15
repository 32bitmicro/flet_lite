from .http_post_request import http_POST_request



def run_page_target():
    url_of_host = open("localhost_api_url.txt", encoding="utf-8").read()

    content = http_POST_request(url=f"{url_of_host}/", post_data={})

    return content