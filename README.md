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
        "source": "globo",
        "publish_date": "2017-05-27 14:00:00",
        "source_description": "No SporTV voc\u00ea encontra a melhor cobertura em v\u00eddeos sobre todos os  Esportes no         Brasil e no Mundo: campeonatos, classifica\u00e7\u00f5es, resultados, atletas e not\u00edcias.",
        "link": "http://sportv.globo.com/site/combate/noticia/2017/05/munhoz-analisa-stasiak-meu-jiu-jitsu-e-melhor-mais-lapidado-do-que-o-dele.html",
        "title": "Munhoz analisa Stasiak: \"Meu jiu-j\u00edtsu \u00e9 melhor, mais lapidado do que o dele\"",
        "top_image": "http://s.glbimg.com/es/ge/f/original/2014/05/31/pedromunhoz_matthobar_ufc_tuf3_ribolli5.jpg",
        "authors": [
            "Marcelo Barone"
        ],
        "text": "Faixa-preta de jiu-j\u00edtsu espera anotar mais um nocaute ou nova finaliza\u00e7\u00e3o (Foto: Marcos Ribolli)\n\nQuando a luta se desenvolve no ch\u00e3o, Pedro Munhoz sente o conforto de quem soma oito de 13 vit\u00f3rias por ..."
    },
    
    {
        "source": "globo",
        "publish_date": "2017-05-23 12:32:00",
        "source_description": "No SporTV voc\u00ea encontra a melhor cobertura em v\u00eddeos sobre todos os  Esportes no         Brasil e no Mundo: campeonatos, classifica\u00e7\u00f5es, resultados, atletas e not\u00edcias.",
        "link": "http://sportv.globo.com/site/programas/redacao-sportv/noticia/2017/05/rizek-alerta-ceni-para-que-nao-vire-novo-dunga-caminho-do-rancor.html",
        "title": "Rizek alerta Ceni para que n\u00e3o vire \"novo Dunga\": \"Caminho do rancor\"",
        "top_image": "http://s.glbimg.com/es/ge/f/original/2017/05/23/ceni.png",
        "authors": [],
        "text": "\n\n\n\n\n\n\n\nT\u00e9cnico do S\u00e3o Paulo, Rog\u00e9rio Ceni, durante a participa\u00e7\u00e3o no \"Bem, Amigos!\", nesta segunda-feira, comentou a sua rela\u00e7\u00e3o com a imprensa e disse \"n\u00e3o ligar\" para o que \u00e9 falado ou escrito a respeito de seu trabalho no Tricolor Paulista (assista ao v\u00eddeo). Ao analisar a declara\u00e7\u00e3o, o apresentador Andr\u00e9 Rizek viu o ex-goleiro \"acuado\", disse temer que Ceni siga o caminho de Dunga, que ficou marcado pelo mau relacionamento com jornalistas, e aconselhou o treinador.\n\n\n\n- Como tenho muita admira\u00e7\u00e3o pelo Rog\u00e9rio e muito respeito, espero que ele n\u00e3o abrace o caminho que o Dunga escolheu na profiss\u00e3o de treinador, que \u00e9 o caminho do rancor e \u00e9 o caminho que d\u00e1 uma relev\u00e2ncia que n\u00e3o merecemos e n\u00e3o temos, uma import\u00e2ncia que n\u00e3o temos, Rog\u00e9rio! Sinceramente, o bom \u00e9 o di\u00e1logo, a troca de ideias. A gente vai se equivocar para caramba em coment\u00e1rios, an\u00e1lises e not\u00edcias dadas, mas esse caminho do rancor derrubou o t\u00e9cnico da sele\u00e7\u00e3o brasileira e fez ele nunca mais trabalhar no futebol brasileiro porque ningu\u00e9m quer algu\u00e9m rancoroso assim - disse, no \"Reda\u00e7\u00e3o SporTV\".\n\n\n\nRog\u00e9rio Ceni, t\u00e9cnico do S\u00e3o Paulo (Foto: Reprodu\u00e7\u00e3o SporTV)\n\nDurante o \"Bem, Amigos!\", Ceni reclamou das abordagens em rela\u00e7\u00e3o ao seu trabalho e aproveitou para dar uma alfinetada, ao lembrar do caso da prancheta chutada por ele e a repercuss\u00e3o do caso.\n\n\n\n- Esses dias o C\u00edcero entrou na minha sala e disse: \"voc\u00ea viu o que 'os caras\" est\u00e3o fazendo com a gente?\". Eu disse \"n\u00e3o vi, estou trabalhando\". Ent\u00e3o, n\u00e3o ligo para o que voc\u00eas falam, escrevem, desde que n\u00e3o atinjam a moral da pessoa, eu n\u00e3o ligo, com rela\u00e7\u00e3o \u00e0 atitude do Rodrigo Caio (caso de fair play) ou com rela\u00e7\u00e3o a chutar qualquer coisa no vesti\u00e1rio. Trinta dias depois foram lembrar da prancheta porque o S\u00e3o Paulo foi eliminado na Sul-Americana e perdeu para o Cruzeiro no primeiro jogo. Faz parte. Tev\u00ea eu assisto pouco, assisto voc\u00eas, os canais fechados um pouco mais. Mas entendo, 24 horas no ar de programa\u00e7\u00e3o tem que falar at\u00e9 de chute em copa d'\u00e1gua, garrafa, porque preencher uma grade de programa\u00e7\u00e3o n\u00e3o \u00e9 das coisas mais f\u00e1ceis - considerou.\n\n\n\nRizek viu sinais de \"rancor\" na declara\u00e7\u00e3o e percebeu \"desgostoso\" com a imprensa. O apresentador considerou o treinador bem informado para quem diz acompanhar pouco as not\u00edcias a respeito do clube. Para o jornalista, o comandante tricolor tem dado import\u00e2ncia excessiva para os jornalistas e comentaristas.\n\n\n\n- O Ceni claramente n\u00e3o est\u00e1 habituado a lidar com isso como treinador. Como jogador, ele respondia s\u00f3 sobre as pol\u00eamicas dele. Agora, qualquer coisinha o treinador tem que responder no S\u00e3o Paulo. Ele foi ao \"Bem, Amigos!\" na entrevista p\u00f3s-jogo e tinha muito rancor com a cobertura da imprensa e os coment\u00e1rios que s\u00e3o feitos em rela\u00e7\u00e3o ao S\u00e3o Paulo. Mesmo ele dizendo que n\u00e3o acompanha, vi ele muito desgostoso com a repercuss\u00e3o do trabalho dele - avaliou o jornalista.\n\n\n\nAcho que o Ceni est\u00e1 se sentindo acuado porque como jogador ele era 90% do tempo elogiado, como mito, l\u00edder e capit\u00e3o. Andr\u00e9 Rizek, apresentador do SporTV\n\nRizek disse que o treinador ter\u00e1 de aprender a lidar melhor com a press\u00e3o e n\u00e3o pode esperar, como treinador, que ela tenha a mesma propor\u00e7\u00e3o da \u00e9poca em que ele atuava como goleiro do S\u00e3o Paulo.\n\n\n\n- Acho que ele est\u00e1 se sentindo acuado porque como jogador ele era 90% do tempo elogiado, como mito, l\u00edder, capit\u00e3o, ele n\u00e3o era questionado se o ataque n\u00e3o funcionava ou o zagueiro n\u00e3o marcava de cabe\u00e7a. No Brasil, o treinador responde por tudo (...) Qualquer treinador na posi\u00e7\u00e3o dele do S\u00e3o Paulo, com tr\u00eas elimina\u00e7\u00f5es, mesmo n\u00e3o sendo culpa exclusiva do t\u00e9cnico, vai sofrer press\u00e3o e responder sobre isso. \u00c9 por essa raz\u00e3o que o Muricy (Ramalho) est\u00e1 muito mais soltinho como comentarista do que como treinador. \u00c9 uma profiss\u00e3o de muita press\u00e3o no Brasil, a qual o Rog\u00e9rio ainda n\u00e3o est\u00e1 habituado - disse.\n\n\n\nAp\u00f3s as elimina\u00e7\u00f5es no Paulista, na Copa do Brasil e na Sul-Americana, o Tricolor aposta todas as fichas no Campeonato Brasileiro. Nesta segunda, a equipe venceu o Ava\u00ed no Morumbi (2 a 0) depois de ter perdido para o Cruzeiro na estreia (1 a 0). O pr\u00f3ximo compromisso \u00e9 o cl\u00e1ssico contra o Palmeiras, s\u00e1bado, \u00e0s 19h, novamente diante da torcida.\n\n\n\n+ Rog\u00e9rio Ceni: \"Talvez Rodrigo Caio e Tite sejam pessoas melhores que eu\"\n\n\n\n+ Ceni admite que n\u00e3o esperava tanta dificuldade como t\u00e9cnico do S\u00e3o Paulo\n\n"
    },
}
```

## TODO
see [news_pool](http://newspaper.readthedocs.io/en/latest/user_guide/advanced.html)


