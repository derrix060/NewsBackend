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
        "category": "top_news"
    },
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
[
  {
    "top_image": "http://computerworld.com.br/sites/beta.computerworld.com.br/files/news_articles/airbus.jpg",
    "authors": [],
    "source_description": "",
    "title": "LastPass agora oferece backup na nuvem para autentica\u00e7\u00e3o de dois fatores",
    "link": "http://computerworld.com.br/lastpass-agora-oferece-backup-na-nuvem-para-autenticacao-de-dois-fatores",
    "text": "O gerenciador de senhas LastPass agora conta com um recurso de backup na nuvem para quem escolher utilizar sua solu\u00e7\u00e3o de autentica\u00e7\u00e3o de dois fatores por meio do aplicativo LastPass Authenticator.\n\nDesta forma, o usu\u00e1rio que optar pela nova funcionalidade n\u00e3o ter\u00e1 mais problemas neste sentido em caso de perda ou roubo do se...",
    "source": "computerworld",
    "publish_date": "2017-05-22 15:44:09-03:00"
  },
  {
    "top_image": "http://computerworld.com.br/sites/beta.computerworld.com.br/files/news_articles/airbus.jpg",
    "authors": [],
    "source_description": "",
    "title": "IoT abrir\u00e1 novas oportunidades para setor de telecom, afirma Bain & Company",
    "link": "http://computerworld.com.br/iot-abrira-novas-oportunidades-para-setor-de-telecom-afirma-bain-company",
    "text": "O potencial de crescimento de Internet das Coisas (IoT), que deve movimentar mais de US$ 470 bilh\u00f5es por ano at\u00e9 2020, segundo estimativas da Bain & Company, \u00e9 ineg\u00e1vel. Mas quem ser\u00e1 respons\u00e1vel pelo suporte de uma infraestrutura t\u00e3o complexa que conecta diversos tipos de tecnologias e dispositivos? Estudo da consultoria Close to Core, ...",
    "source": "computerworld",
    "publish_date": "2017-05-22 13:35:39-03:00"
  }
]
```

## Update news

To update news for each 10 minutes, make a request to https://dsnewsbackend.mybluemix.net/api/news/update_all_news/updateNews



