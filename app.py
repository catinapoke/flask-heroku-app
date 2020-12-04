# flask-heroku-app
from words_api import *
from flask import Flask
from flask import render_template, request
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html", title="LOTR")


@app.route('/sentences', methods=['POST'])
def find_sentences():
    words_str = request.form.get('words').split(';')
    examples_number = request.form.get('examples')

    sentences = get_sentences_from_file('lotr.txt')
    correct_sentences = find_words(sentences, words_str, int(examples_number))['words']

    return render_template('sentences.html', correct_sentences=correct_sentences)


def comma_separated_params_to_list(param: str):
    seps = ' \"'
    param = param.lstrip('[').rstrip(']')
    result = []
    for val in param.split(','):
        if val:
            result.append(val.lstrip(seps).rstrip(seps))
    return result


@app.route('/request_sentences')
def custom_route():
    words_str = comma_separated_params_to_list(request.args.get("words"))
    examples_number = request.args.get('examples')

    sentences = get_sentences_from_file('lotr.txt')
    correct_sentences = find_words(sentences, words_str, int(examples_number))
    correct_sentences['words_str'] = words_str
    correct_sentences['examples'] = examples_number
    return f'{correct_sentences}'


if __name__ == '__main__':
    app.run()
