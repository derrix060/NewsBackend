import newspaper

cnn_paper = newspaper.build('https://www.uol.com.br/', language='pt', memoize_articles=False)

"""
for category in cnn_paper.category_urls():
    print(category)
"""
"""
for article in cnn_paper.articles:
    print(article.url)
"""

article = newspaper.Article(url='http://revistatrip.uol.com.br/tpm/a-viuva-do-chorao-graziela-goncalves-em-um-depoimento-sobre-seus-dias-de-luto')
article.download()
article.parse()
print(article.text)
"""
article = newspaper.Article(url='http://g1.globo.com/politica/operacao-lava-jato/noticia/pf-comeca-pericia-nos-gravadores-entregues-pela-defesa-de-joesley-batista.ghtml')
article.download()
article.parse()
print(article.text)
"""


"""
PT -> UOL
EN -> CNN http://cnn.com
FR -> http://www.lemonde.fr

"""