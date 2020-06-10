import requests
import scrapy


class BlogSpider(scrapy.Spider):
    name = 'seloger'



    def start_requests(self):
        start_urls = "https://www.seloger.com/list.html?projects=2&types=2&natures=1,2&isochronepoints=[{%22id%22:0,%22point%22:{%22lat%22:48.266549,%22lng%22:3.255339,%22mode%22:{%22type%22:%22Car%22,%22place%22:0,%22options%22:{%22rushHour%22:true}}},%22timeRange%22:[1800]}]&price=NaN/220000&enterprise=0&qsVersion=1.0"
    
        # Set the headers here. The important part is "application/json"
        headers =  {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        yield scrapy.http.Request(start_urls, headers=headers)


    def parse(self, response):
        for title in response.css('header.headersl div.c-header-container a'):
            yield {'title': title.css('a ::text').get()}
            