import newspaper


cnn_paper = newspaper.build('http://computerworld.com.br/', language='pt',
                             memoize_articles=False, fetch_images=False)

for art in cnn_paper.articles:
    print(art.url)