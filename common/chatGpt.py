from revChatGPT.V3 import Chatbot
from config import API_KEY


def get_from_gpt(prompt):
    chatbot = Chatbot(api_key=API_KEY)
    res = chatbot.ask(prompt)
    return res
