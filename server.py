from flask import Flask, render_template, request
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Python News'
    city = 'Almaty, Kazakhstan'
    weather = weather_by_city(city)
    return render_template('index.html', page_title=title, weather=weather)

if __name__ == '__main__':
    app.run(debug=True)