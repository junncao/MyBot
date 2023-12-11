from revChatGPT.V3 import Chatbot
from config import API_KEY_OPENAI, API_KEY_SB

import os

os.environ["API_URL"] = "https://api.openai-sb.com/v1/chat/completions"


def get_from_gpt(prompt):
    chatbot = Chatbot(api_key=API_KEY_SB)
    res = chatbot.ask(prompt)
    return res


if __name__ == "__main__":
    res = get_from_gpt("hello")
    print(res)
