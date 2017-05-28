from flask import Flask, jsonify
from app.newspaper import Newspaper
from os.path import abspath
import json
import time


app = Flask(__name__)

languages = ['pt', 'en']
categories = ['last_news','sports', 'economy', 'health', 'tech']


f = open(abspath('./app/sources.json'), 'r')
sources = json.loads(f.read())
f.close
srcs = {}
for src in sources['sources']:
    print(src)
    srcs[src['language'] + '_' + src['category']] = Newspaper(src['language'],
                                                              src['category'],
                                                              src['link'],
                                                              src['keyword'])


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/news/languages')
def get_languages():
    return jsonify(languages)


@app.route('/api/news/categories')
def get_categories():
    cat = []
    for cate in categories:
        cat_d = {}
        cat_d['category'] = cate
        cat.append(cat_d)
    return jsonify(cat)


@app.route('/api/news/sources_generate')
def generate_json():
    for lang in languages:
        for cat in categories:
            f = open('./app/news/' + lang + '_' + cat + '.json', 'w+')
            f.close()


@app.route('/api/news/<language>/<category>')
def top_news(language, category):
    return srcs[language + "_" + category].getArticles()


@app.route('/api/news/update_news/<passwd>')
def update_news(passwd):
    if passwd == 'updateNews':
        while True:
            print('sleeping for 600 secs...')
            time.sleep(600)
            for src in sources['sources']:
                srcs[src['language'] + '_' + src['category']].refreshArticles()
            print('Articles up-to-date!')
    else:
        return('Sorry, wrong password!')
