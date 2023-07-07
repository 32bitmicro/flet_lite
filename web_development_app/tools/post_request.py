import sys


def http_POST_request (url, post_data):
    if sys.platform == "emscripten":
        from js import XMLHttpRequest, Blob
        import json

        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }

        data = post_data

        req = XMLHttpRequest.new()
        req.open("POST", f"{url}", False, crossorigin="anonymous", headers=headers)
        blob = Blob.new([json.dumps(data)], {type : 'application/json'})
        req.send(blob)

        return str(req.response)
    else:
        import requests

        r = requests.post(url=f"{url}", verify=False, data=post_data, json=post_data)
        return str(r.text)