from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs

from webapp.model import db, News


def get_news(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Network error')
        return False


def get_python_news():
    html = get_news('https://www.python.org/blogs/')
    if html:
        soup = bs(html, 'html.parser')
        news_list = soup.find('ul', class_='list-recent-posts').findAll('li')
        for news in news_list:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
<<<<<<< HEAD
                published = datetime.strptime(published, "%B %d,%Y")
=======
                published = datetime.strptime(published, "%B %d, %Y")
>>>>>>> 95cd575fecb7da49756cacfa75e77250b7cab8e6
            except(ValueError):
                published = datetime.now()
            save_news_todb(title, url, published)


def save_news_todb(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()

