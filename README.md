# NewsBackend: Concentrate news in one endpoing

This is a service to get top news in different languages and categories.

## Languages
You can see our available languages on this endpoint: https://dsnewsbackend.mybluemix.net/api/news/languages

```json
[
    "pt",
    "en"
]
```

## Categories
You can see our available categories on this endpoint: https://dsnewsbackend.mybluemix.net/api/news/categories

```json
[
    {
        "category": "sports"
    },
    {
        "category": "economy"
    },
    {
        "category": "health"
    },
    {
        "category": "tech"
    }
]
```

## News
To get top news, you need to choose the language and the category. After this, use this endpoing: https://dsnewsbackend.mybluemix.net/api/news/{language}/{category}

This is an example of return:
```json
{
    {
        "title": "Brook vs Spence Jr: Kell Brook beaten by Errol Spence Jr at Bramall Lane in Sheffield",
        "text": "Brook vs Spence Jr: Kell Brook beaten by Errol Spence Jr at Bramall Lane in Sheffield\n\nKell Brook was stopped by Errol Spence Jr in the penultimate round after succumbing to an eye injury at Bramall Lane in Sheffield on Saturday night...",
        "top_image": "http://someCDN.com/blah/blah/blah/file.png",
        "authors": ["Mc Jackson", "Paul Jhon"],
        "keywords": ["New Years", "resolution"],
        "source": "Cnn",
        "source_description": "CNN.com delivers the latest breaking news and information on the latest...",
        "link": "http://www.bbc.com/news/world-europe-40077241",
        "publish_date": "20/02/1970 - 10:40"
    },
    {
        "title": "Other title",
        "text": "Other text...",
        "top_image": "http://someCDN.com/blah/blah/blah/file.png",
        "authors": ["Mc Jackson", "Paul Jhon"],
        "keywords": ["New Years", "resolution"],
        "source": "Cnn",
        "source_description": "CNN.com delivers the latest breaking news and information on the latest...",
        "link": "http://www.bbc.com/news/world-europe-40077241",
        "publish_date": "20/02/1970 - 10:40"
    }
}
```

## TODO
see [news_pool](http://newspaper.readthedocs.io/en/latest/user_guide/advanced.html)


