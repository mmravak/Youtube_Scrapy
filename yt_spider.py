import scrapy

class YoutubeSpider(scrapy.Spider):
    
    name = "YoutubeSpider"
    
    start_urls = []
    #start_urls = ['https://www.youtube.com/watch?v=Tc0tLGWIqxA']

    input_file = open('yt_links.txt', 'r')

    for link in input_file:
      start_urls.append(link)

    def parse(self, response):
        
        #print(response.text)

        yield {
            'title': response.xpath('//meta[@name="title"]/@content').get(),
            'datePublished': response.xpath('//meta[@itemprop="datePublished"]/@content').get(),
            'genre': response.xpath('//meta[@itemprop="genre"]/@content').get(),
            'publisher' : response.xpath('//link[@itemprop="name"]/@content').get(),
            'viewsCount' : response.xpath('//meta[@itemprop="interactionCount"]/@content').get()
        }
