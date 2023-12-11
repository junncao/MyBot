import requests
import json

from common.kimBot import send_message


def google_search(search_term, api_key, cse_id, **kwargs):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id,
        **kwargs
    }
    response = requests.get(url, params=params)
    return response.json()


search_term = "telegram groups"
api_key = "AIzaSyDjvYPfGvd5hjKtYMMOeLwoOecUwfoej1M"  # 你的API密钥
cse_id = "a0b735e13d6864662"  # 你的自定义搜索引擎ID
if __name__ == "__main__":

    results = google_search(search_term, api_key, cse_id)

    print(results)
    results_str = ""
    for result in results['items']:
        title = result['title']
        link = result['link']
        results_str += "Title: " + title + "\nLink: " + link + "\n"
    send_message(results_str)

