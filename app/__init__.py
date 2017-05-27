from flask import Flask, jsonify
from app.news import News
from app.newspaper import Newspaper
from os.path import abspath
import json


app = Flask(__name__)

languages = ['pt', 'en', 'zh']
categories = ['sports', 'economy', 'health', 'tech', 'study']


f = open(abspath('./app/sources.json'), 'r')
sources = json.loads(f.read())
f.close
srcs = {}
for src in sources['sources']:
    print(src)
    srcs[src['language'] + '_' + src['category']] = Newspaper(src['language'],
                                                        src['category'],
                                                        src['link'])


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
    srcs_json = []
    for lang in languages:
        for cat in categories:
            s = {}
            s['link'] = ''
            s['language'] = lang
            s['category'] = cat
            srcs_json.append(s)
    return jsonify(srcs_json)


@app.route('/api/<language>/<category>/top_news')
def top_news(language, category):
    return jsonify(srcs[language + "_" + category].getArticles())
