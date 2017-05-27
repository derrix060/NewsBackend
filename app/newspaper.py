import newspaper
import json


class Newspaper():

    def __init__(self, language, category, link):
        print('link: ' + str(link))
        self.link = link
        self.language = language
        self.category = category
        self.path = './app/news/' + self.language + '_' + self.category + '.json'
        # Download newest news
        # self.refreshArticles()

    def refreshArticles(self):
        self.news = newspaper.build(self.link, language=self.language,
                                    memoize_articles=False,
                                    fetch_images=False)
        self.articles = self.news.articles
        articles = self.downloadArticles(amount=2)
        articles = json.dumps(articles)
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
                print(article_temp.url)
                article_temp.download()
                article_temp.parse()

                if len(article_temp.text) > 750:
                    article = {}
                    article['title'] = article_temp.title
                    article['text'] = article_temp.text
                    article['publish_date'] = str(article_temp.publish_date)
                    rtn.append(article)
                    i += 1
            except Exception as e:
                print(e)
        return rtn
