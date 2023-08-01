import time

from common.kimBot import send_message


def send_articles():
    articles = []
    article_body = ""
    with open("IELTS_article.txt", "r") as f:
        for line in f:
            if line.strip().startswith('**') and line.strip().endswith('**'):  # 新文章的标题
                if article_body:  # 如果已有文章正文，那么添加到文章列表中
                    articles.append(article_body.strip())
                    article_body = ""  # 重置文章正文
                articles.append(line.strip().strip('**'))  # 添加新文章的标题
            else:
                article_body += line  # 添加到文章正文

        if article_body:  # 添加最后一篇文章的正文
            articles.append(article_body.strip())

    for i in range(0, len(articles), 2):  # 每隔两个元素（一个标题和一个正文）为一篇文章
        title = articles[i].strip()
        body = articles[i+1].strip()
        message = f"{title}\n\n{body}"
        send_message(message)
        time.sleep(3600)  # 每隔1小时发送一篇文章
if __name__ == "__main__":
    send_articles()  # 开始立即发送文章，每隔1小时发送一篇
