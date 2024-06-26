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
    city = request.args.get('city', '').strip() or 'London'

    weather_data = get_current_weather(city)

    if weather_data.get('cod') != 200:
        return render_template("not-found.html", city=city)
    else:
        return render_template(
            "weather.html",
            title=weather_data.get("name", "Unknown City"),
            status=weather_data["weather"][0]["description"] if weather_data.get(
                "weather") else "No data",
            temp=f'{weather_data["main"]["temp"]:.1f}' if weather_data.get(
                "main") else "N/A",
            feels_like=f'{weather_data["main"]["feels_like"]:.1f}' if weather_data.get(
                "main") else "N/A"
        )

# Using development server
# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=8000)


# Using production server
if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
