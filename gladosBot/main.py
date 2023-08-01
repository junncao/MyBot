import csv
import requests
import time
from datetime import datetime
import json

from common.kimBot import send_message
from config import webhook

LOG_PATH = "log.txt"
CSV_PATH = "data.csv"


def main():
    while True:
        with open(LOG_PATH, 'a') as log_file:
            time_now = datetime.now()
            log_file.write(str(time_now) + "\n")

            with open(CSV_PATH, 'r') as csv_file:
                reader = csv.reader(csv_file)
                for i, row in enumerate(reader):
                    host = row[0]
                    cookie = row[1]
                    tag = row[2]

                    headers = {
                        'authority': 'glados.rocks',
                        'accept': 'application/json, text/plain, */*',
                        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
                        'content-type': 'application/json;charset=UTF-8',
                        'cookie': cookie.strip(),
                        'origin': 'https://glados.rocks',
                        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
                    }

                    res = requests.post(host, headers=headers, json={"token": "glados.one"})

                    body = res.text
                    data_dict = json.loads(body)
                    code = data_dict["code"]
                    message = data_dict["message"]
                    log_file.write(f"index = {i}, name = {tag}, code = {code} message={message}\n")
                    print(f"index = {i}, name = {tag}, code = {code} message={message}\n")

                    if code != 0 and not str(message).startswith("Please Try Tomorrow"):
                        send_message(webhook=webhook, message=f"glados: {tag} {body}")

            time.sleep(8 * 60 * 60)  # Execute once every 8 hours


if __name__ == "__main__":
    main()
