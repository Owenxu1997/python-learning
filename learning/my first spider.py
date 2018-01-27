import requests
from bs4 import BeautifulSoup


def video_spider():
    while (1):
        url = 'http://www.youku.com'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'tittle':'张韶涵撒柔情唱哭全场'}):
            href = 'http://www.youku.com' + link.get('href')
            print(href)

video_spider()