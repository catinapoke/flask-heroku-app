# flask-heroku-app
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World, that Flask app for testing Heroku hosting!'


@app.route('/<custom_url>')
def custom_route(custom_url):
    return f'You at sub-page {custom_url}'


if __name__ == '__main__':
    app.run()
