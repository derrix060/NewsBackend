from newspaper import Article
import app


class News():

    def __init__(self, url, language):
        self.article = Article(url, language=language)
        self.article.download()
        self.article.parse()
        self.article.nlp()

    @property
    def title(self):
        return self.article.title

    @property
    def text_content(self):
        return self.article.text

    @property
    def summary(self):
        return self.article.summary
