from flask import Flask, jsonify
from app.news import News
from app.source import Source
from os.path import abspath
app = Flask(__name__)

languages = ['pt', 'en', 'zh']
categories=['sports', 'economy', 'politics', 'health', 'tech', 'study']

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/languages')
def get_languages():
    return jsonify(languages=languages)


@app.route('/categories')
def get_categories():
    return jsonify(categories=categories)

@app.route('/sources_generate')
def generate_json():
    srcs = []
    for lang in languages:
        for cat in categories:
            s = {}
            s['link'] = ''
            s['language'] = lang
            s['category'] = cat
            srcs.append(s)
    return jsonify(srcs)

@app.route('/sources')
def get_sources():
    f = open(abspath('./app/sources.json'), 'r')
    rtn = f.read()
    f.close
    return rtn
