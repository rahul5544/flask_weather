import requests
from flask import Flask, render_template, request

app  = Flask(__name__)
app.config['DEBUG'] = True
app=Flask(__name__,template_folder='templates')
from app import app


@app.route('/' , methods=['GET' , 'POST'])
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=Enter your app id'
    city = 'bhubaneswar'
    r = requests.get(url.format(city)).json()
    footer = 'Developed by Rahul'
    print(r)
    weather = {
        'city': city , 
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    print(weather)
    # return f"{weather}"
    return render_template('weather.html' , weather = weather , footer = footer)
    # app.add_url_rule(‘/’, ‘hello’, hello_world) # to call from different url end point
