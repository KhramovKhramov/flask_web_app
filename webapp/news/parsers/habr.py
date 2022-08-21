from datetime import datetime

from bs4 import BeautifulSoup
from webapp.news.parsers.utils import get_html, save_news


def get_habr_snippets():
    html = get_html('https://habr.com/ru/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except (ValueError):
                published = datetime.now()
            save_news(title, url, published)
