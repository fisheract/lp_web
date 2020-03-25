import os

basedir = os.path.abspath(os.path.dirname(__file__))

API_KEY = 'd71e070d8cbd4b0ba2d73005200103'
WEATHER_DEFAULT_CITY = "Almaty, Kazakhstan"
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SECRET_KEY = "5+XBN&?LqJpx#JPNBAa$v@-4HJS5ANnw#d8846n3cqK-KsG%f*wBVCc%ewhY-5y$H-r+%*C3qU4ZJ^kYGyZHqZYSgq$hkLP2zJ_%YLE5=+Cjt+Xgdpq6yFs#V#Yd-YWHJ=9$RcyfqS=?KJC+_qeuscLTr$JY95=#J9Cky4kTF9nhxvMs^ZD_ZgDDpWdHRFznG_SQ^%2C^T#peWCX&%97H=aeF3bSYKYMPK!LN^pAPJ7P=sH^@ujEyqX5%ZeEfxhC"