import json
import os
from datetime import datetime
import random
import time

import requests
import schedule
from revChatGPT.V3 import Chatbot

FEISHU_WEB_HOOK = "https://open.feishu.cn/open-apis/bot/v2/hook/2e05457e-0d7d-4240-b895-34ec6f0cc377"
KIM_WEB_HOOK = "https://kim-robot.kwaitalk.com/api/robot/send?key=ac6a78c1-ef13-4fd8-a06a-b8f538175e32"
API_KEY_SB = "sb-91dd7e906a7e675931eb29d3ad30d5d6dbcd828650b78203"
os.environ["API_URL"] = "https://api.openai-sb.com/v1/chat/completions"
prompt_txt = 'leetcode.txt'

leetcode_prompt = """
Please use Chinese, with detailed descriptions and examples, to provide the following LeetCode questions, descriptions, solution ideas and Kotlin code.
Make sure your description is clear and includes the requirements and constraints of the issue. The idea of solving the problem should be explained step-by-step, including the key steps of the algorithm and the selection of data structures. Finally, please provide the solution code written in Kotlin to ensure that the code is readable and correct.
Note that your answer should be flexible to allow for different solutions and code implementations.this is the question name:
"""


def send_kim(message, webhook=KIM_WEB_HOOK):
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


def send_feishu(message, webhook=FEISHU_WEB_HOOK):
    headers = {'Content-Type': 'application/json'}
    data = {
        "msg_type": "text",
        "content": {
            "text": message
        }
    }
    response = requests.post(webhook, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)


def get_from_gpt(prompt):
    chatbot = Chatbot(api_key=API_KEY_SB)
    res = chatbot.ask(prompt)
    return res


def get_random_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return random.choice(lines)


def main():
    time_now = datetime.now()
    print(time_now)
    line = get_random_line(prompt_txt)
    print(line)
    res = get_from_gpt(leetcode_prompt + line)
    print(res)
    send_feishu(line + "\n" + res)
    send_kim(line + "\n" + res)
    # time.sleep(60 * 60 * 2)


if __name__ == "__main__":
    main()
    schedule.every().day.at("08:00").do(main)
    schedule.every().day.at("12:00").do(main)
    schedule.every().day.at("21:00").do(main)

    # 运行调度任务
    while True:
        schedule.run_pending()
        time.sleep(1)  # 短暂休眠以减少循环的CPU使用率
