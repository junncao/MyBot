import json
import time
import requests
from pdf2image import convert_from_path

from gptBot.oneHour import FEISHU_WEB_HOOK


def convert_and_upload(pdf_path, start_page, url, key):
    # 创建临时目录保存图片
    # 获取 PDF 总页数
    total_pages = len(convert_from_path(pdf_path))

    # 从指定开始页逐页处理
    for i in range(start_page - 1, total_pages):
        # 每次处理一张图片，每张图片单独发送
        images = convert_from_path(pdf_path, first_page=i + 1, last_page=i + 1)
        for image in images:
            image_path = f"temp_images/page_{i + 1}.png"
            image.save(image_path, 'PNG')

            with open(image_path, 'rb') as file_obj:
                files = {
                    'type': (None, 'image'),
                    'key': (None, key),
                    'media': (image_path, file_obj, 'image/png')
                }

                # 发送 POST 请求
                response = requests.post(url, files=files)

                if response.status_code == 200:
                    response_data = response.json()
                    media_id = response_data.get("media_id")
                    sendPhoto(media_id)
                    print(f"Media ID for page {i + 1}: {media_id}")
                else:
                    print(f"Error on page {i + 1}: {response.status_code}, Response: {response.text}")
        if i % 3 == 2:
            time.sleep(60 * 60 * 2)

        # 确保在发送下一个请求前等待2小时

def sendPhoto(media_id):
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "image",
        "image": {
            "media_id": media_id
        }
    }
    response = requests.post(FEISHU_WEB_HOOK, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)
pdf_path = '/Users/caojun05/Downloads/labuladong的刷题笔记V1.5.pdf'
start_page = 94
url = 'https://kim-robot.kwaitalk.com/api/robot/upload'
key = 'a1f19682-5857-4a01-b1eb-33409d327e62'

if __name__ == '__main__':
    convert_and_upload(pdf_path, start_page, url, key)