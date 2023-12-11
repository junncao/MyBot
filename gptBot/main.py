from datetime import datetime

from common.chatGpt import get_from_gpt
from common.kimBot import send_message

from config import WEB_HOOK

import time
import random


def get_random_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return random.choice(lines)


prompt_txt = 'prompt.txt'

if __name__ == "__main__":
    while True:
        time_now = datetime.now()
        print(time_now)
        line = get_random_line(prompt_txt)
        print(line)
        res = get_from_gpt(line)
        print(res)
        send_message(res)
        time.sleep(60 * 60 * 1)
