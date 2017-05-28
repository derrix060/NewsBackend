import newspaper
from newspaper import Article, news_pool, build
from os.path import abspath
import json
import re


class Newspaper():

    def __init__(self, language, category, link, keyword):
        print('link: ' + str(link))
        self.link = link
        self.language = language
        self.category = category
        self.keyword = keyword
        self.path = abspath('./app/news/' + self.language + '_' + self.category + '.json')
        # Download newest news
        # self.refreshArticles()

    def refreshArticles(self):
        self.news = build(self.link, language=self.language,
                                    memoize_articles=False)
        self.articles = self.news.articles
        articles = self.downloadArticles(amount=10)
        articles = json.dumps(articles, indent=2)
        f = open(self.path, 'w+')
        f.write(str(articles))
        f.close()

    def getArticles(self):
        f = open(self.path, 'r')
        rtn = f.read()
        f.close()
        return rtn

    def downloadArticles(self, amount=10):

        rtn = []
        if amount > len(self.articles):
            amount = len(self.articles)
        i = 0
        j = -1
        while i < amount and j < len(self.articles):
            j += 1
            try:
                article_temp = self.articles[j]
                if self.keyword in article_temp.url:
                    print(article_temp.url)
                    article_temp.download()
                    article_temp.parse()

                    if len(article_temp.text) > 300:
                        article = {}
                        article['title'] = article_temp.title
                        article['text'] = article_temp.text
                        article['top_image'] = article_temp.top_image
                        article['authors'] = article_temp.authors
                        article['source'] = self.news.brand
                        article['source_description'] = self.news.description
                        article['link'] = article_temp.url
                        article['publish_date'] = str(article_temp.publish_date)
                        rtn.append(article)
                        i += 1
            except Exception as e:
                print('exception: ' + str(e))
        return rtn
