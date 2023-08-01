import requests
import json


def send_message(webhook, message):
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    response = requests.post(webhook, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)
