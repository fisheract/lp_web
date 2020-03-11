import os

basedir = os.path.abspath(os.path.dirname(__file__))

API_KEY = 'd71e070d8cbd4b0ba2d73005200103'
WEATHER_DEFAULT_CITY = "Almaty, Kazakhstan"
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')