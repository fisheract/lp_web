import requests
from bs4 import BeautifulSoup as bs

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
        result = []
        for news in news_list:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            result.append({
                'title':title,
                'url':url,
                'published':published
            })
        return result
    return False

