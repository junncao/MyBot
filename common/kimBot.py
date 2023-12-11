import requests
import json

from config import WEB_HOOK


def send_message(message, webhook=WEB_HOOK):
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
