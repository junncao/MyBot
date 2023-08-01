from common.chatGpt import get_from_gpt
from common.kimBot import send_message
import time

from config import webhook

if __name__ == "__main__":
    with open("prompt.txt", "r") as f:
        for line in f:
            res = get_from_gpt(line)
            time.sleep(10)
            send_message(webhook, res)
            
    