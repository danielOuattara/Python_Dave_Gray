from flask import Flask, request, render_template
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = get_current_weather(city)
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"],
        temp=f'{weather_data["main"]["temp"]:.1f}',
        feels_like=f'{weather_data["main"]["feels_like"]:.1f}')


"""Using development server :"""
# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=8000)


"""Using production server :"""
if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
