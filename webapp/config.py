from datetime import timedelta
import os

from webapp import localconfig

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
WEATHER_DEFAULT_CITY = 'Almaty, Kazakhstan'
WEATHER_API_KEY = localconfig.WEATHER_API_KEY
WEATHER_URL = localconfig.WEATHER_URL
SECRET_KEY = localconfig.SECRET_KEY
REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False