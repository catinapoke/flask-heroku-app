# flask-heroku-app
from words_api import *
from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html",
                           title="LOTR")


@app.route('/sentences', methods=['GET', 'POST'])
def find_sentences():
    words_str = request.form.get('words').split(';')
    examples_number = request.form.get('examples')

    sentences = get_sentences_from_file('lotr.txt')
    correct_sentences = find_words(sentences, words_str, int(examples_number))['words']

    return render_template('sentences.html', correct_sentences=correct_sentences)


@app.route('/<custom_url>')
def custom_route(custom_url):
    return f'You at sub-page {custom_url}'


@app.route('/request')
def json_request():
    # двоичное представления
    data = request.data
    print(data)
    # json
    result = {
        "word": json_data["word"],
        "from": json_data["from"],
        "to": json_data["to"],
        "example": [
            "2222222222222222222222222222222",
            "33333333333333333333333333333533"
        ]
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run()
