# Youtube scraper 

Scrapy is a free and open source Python framework used for web scraping a website. It provides tools needed to efficiently extract data from web pages, process and store it in a wanted format and structure.

[![Made withScrapy](https://img.shields.io/badge/Made%20with-Scrapy-green)](https://scrapy.org/)

## Assignment:

Scraping Youtube website

Link: https://www.youtube.com/

## Installation and starting in Colab
[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1H2mExKRjqxSMecIsMgNwBH8_7N17N8RK?usp=sharing)


Install scrapy Python framework using package manager command line:

```
pip install scrapy
```

Importing scrapy library and other required modules (class *CrawlerProcess* from *crawler* module):

```
import scrapy 
from scrapy.crawler import CrawlerProcess
```
Creating web scrapy Spider which is used for crawling over the website and collecting data.

Starting scrapy Spider in Python script:
```
process.crawl(YoutubeSpider)
process.start()
```

Importing extracted data from websites that are exported to a csv file using pandasa:

```
import pandas as pd
yt_data = pd.read_csv('yt_data.csv')
```
## Installation and starting in Visual Studio Code

[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/organization/repository)


Install virtual enviroment in Terminal using command line:
```
py -m venv venv
```
To activate venv go to _View_ tab and select _Command Palette_

Search _Python: Select Interpreter_ -> select _Edit interpreter path_

Choose _python.exe_ from _venv/scripts_

Install packages from _requirements_:
```
pip install -r requirements.txt
```
Run youtube spider:
```
scrapy runspider yt_spider.py -o yt_data.csv
```





## Documentation

- Python: https://docs.python.org/3/
- Scrapy: https://docs.scrapy.org/
- Pandas: https://pandas.pydata.org/docs/

## License
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
#
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
