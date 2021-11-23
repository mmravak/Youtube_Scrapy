# Youtube scrapy 

Scrapy je besplatan i open-source Python okvir koji se primjenjuje za web scrapeanje web stranica. Pruža alate koji su potrebni za učinkovito povlačenje podataka s web stranice, njihovu obradu te pohranu u željenom formatu i strukturi.

[![Made withScrapy](https://img.shields.io/badge/Made%20with-Scrapy-green)](https://scrapy.org/)

## Zadatak:

Web scrapeanje Youtube web stranice

Link: https://www.youtube.com/

## Instalacija i pokretanje       [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1H2mExKRjqxSMecIsMgNwBH8_7N17N8RK?usp=sharing)


Instalacija scrapy Python okvira pomoću *package managera* naredbom:

```
pip install scrapy
```

*Importanje* scrapy biblioteke i ostalih potrebnih modula (klasa *CrawlerProcess* iz *crawler* modula, json modul):

```
import scrapy 
from scrapy.crawler import CrawlerProcess
# import json
```
Kreiranje web scrapy Spidera koji služi za *crawling* po stranici i prikupljanje podataka.

Pokretanje scrapy Spidera u python skripti:
```
process.crawl(YoutubeSpider)
process.start()
```

*Importanje* povučenih podataka s web stranice koji su se *exportali* u csv datoteku pomoću *pandasa*:

```
import pandas as pd
yt_data = pd.read_csv('yt_data.csv')
```
## Dokumentacija

- Scrapy: https://docs.scrapy.org/
- Pandas: https://pandas.pydata.org/docs/

## Licenca
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
