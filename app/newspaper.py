import newspaper


class Newspaper():

    def __init__(self, language, category, link):
        print('link: ' + str(link))
        self.news = newspaper.build(link, language=language,
                                    memoize_articles=False,
                                    fetch_images=False)
        self.articles = self.news.articles
        self.language = language
        self.category = category

    def getArticles(self, amount=10):
        rtn = []
        if amount > len(self.articles):
            amount = len(self.articles)
        i = 0
        j = -1
        while i < amount:
            j += 1
            try:
                article_temp = self.articles[j]
                print(article_temp.url)
                article_temp.download()
                article_temp.parse()

                if len(article_temp.text) > 1000:
                    article = {}
                    article['title'] = article_temp.title
                    article['text'] = article_temp.text
                    rtn.append(article)
                    i += 1
            except Exception as e:
                print(e)
        return rtn