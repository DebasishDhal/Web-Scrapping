Here we scrap the content of the Odia language news channel - https://otvkhabar.in/

The process of scrapping is divided into the following parts: - 

1- Collection of individual article links from OTV website. Articles are bunched under one or more topics like entertainment, sports, economy etc. The links are colllected through
[link_loader](https://github.com/DebasishDhal/Web-Scrapping/blob/main/otv/link_loader.py) script. 

- Once all links are collected, a set is taken of all links, to avoid duplication.
- Now, the links are ready to be scrapped.

2- A single OTV article is scrapped by [single_article_scrapper](https://github.com/DebasishDhal/Web-Scrapping/blob/main/otv/otv_single_article_scrapper.py) script.

3- We take one article link at a time, scrap it, add it to our existing scrapped content, save the scrapped content. [Script](https://github.com/DebasishDhal/Web-Scrapping/blob/main/otv/continious_otv_news_scrapping.py). I repeated this for 3-4 days. 

- 9M tokens were scrapped in total through this method.
- The only problem is that Colab has a memory issue. The disk gets filled up rapidly, even though I am not saving much in the colab disk space (~100GB).
- And rapidly reading and writing files on Drive causes some problems.
- I'd say it's best to do this on your local system.
