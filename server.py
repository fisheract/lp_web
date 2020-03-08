from flask import Flask, render_template, request

from news import get_python_news
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Python News'
    city = 'Almaty, Kazakhstan'
    weather = weather_by_city(city)
    news_list = get_python_news()
    return render_template('index.html', page_title=title, weather=weather, news_list=news_list)

if __name__ == '__main__':
    app.run(debug=True)