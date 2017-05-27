from flask import Flask, jsonify
from app.news import News
from app.newspaper import Newspaper
from os.path import abspath
import json


app = Flask(__name__)

languages = ['pt', 'en']
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


@app.route('/api/languages')
def get_languages():
    return jsonify(languages=languages)


@app.route('/api/categories')
def get_categories():
    return jsonify(categories=categories)


@app.route('/api/sources_generate')
def generate_json():
    for lang in languages:
        for cat in categories:
            f = open('./app/news/' + lang + '_' + cat + '.json', 'w+')
            f.close()


@app.route('/api/<language>/<category>')
def top_news(language, category):
    return jsonify(srcs[language + "_" + category].getArticles())
