import newspaper


class Newspaper():

    def __init__(self, language, category, link):
        print('link: ' + str(link))
        self.news = newspaper.build(link, language=language, memoize_articles=False)
        self.articles = self.news.articles
        self.language = language
        self.category = category

    def getArticles(self, amount=10):
        rtn = []
        if amount > len(self.articles):
            amount = len(self.articles)
        for i in range(amount):
            try:
                article_temp = self.articles[i]
                print(article_temp.url)
                article_temp.download()
                article_temp.parse()
                article = {}
                article['title'] = article_temp.title
                article['text'] = article_temp.text
                rtn.append(article)
            except Exception as e:
                print(e)
        return rtn