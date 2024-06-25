from flask import Flask, request, render_template
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello Flask'


if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0", port=8000)
    serve(app, host="0.0.0.0", port=8000)
