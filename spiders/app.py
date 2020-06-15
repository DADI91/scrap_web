import scrapy
import time
import json

class LeBonCoinSpider(scrapy.Spider):
    name = "LeBonCoin"

    def start_requests(self):

        #url = "https://www.seloger.com/list.htm?types=1&projects=1&enterprise=0&places=%5B%7Bdiv%3A2238%7D%5D&qsVersion=1.0"

        #url = "https://www.seloger.com/list.htm?types=1&projects=1&enterprise=0&places=%5B%7Bdiv%3A2238%7D%5D&qsVersion=1.0"

        url = "https://www.seloger.com/immobilier/locations/bien-appartement/ile-de-france.htm?projects=1&types=1&places=[{cp:75}]&price=NaN/1200&rooms=3&enterprise=0&qsVersion=1.0"

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

        yield scrapy.http.Request(url, headers=headers)



    def parse(self,response):
        # //div[@id="images"]/a/text()
        # div.fMfqlk
        annonce = []
        for annonce in response.css('div.fMfqlk'):
            yield {
                'piéces': annonce.css('div.Card__ContentZone-sc-7insep-3.gfORyM > div.ContentZone__DetailTop-wghbmy-6.dPYwvZ > div:nth-child(1) > ul > li:nth-child(1)::text').get()[0:1],
                'chambres': annonce.css('div.Card__ContentZone-sc-7insep-3.gfORyM > div.ContentZone__DetailTop-wghbmy-6.dPYwvZ > div:nth-child(1) > ul > li:nth-child(2)::text').get()[0:1],
                'surface': annonce.css('div.Card__ContentZone-sc-7insep-3.gfORyM > div.ContentZone__DetailTop-wghbmy-6.dPYwvZ > div:nth-child(1) > ul > li:nth-child(3)::text').get(),
                'prix': annonce.css('div.Card__ContentZone-sc-7insep-3.gfORyM > div.ContentZone__DetailTop-wghbmy-6.dPYwvZ > div.Price__PriceContainer-sc-1g9fitq-0.eOPseM > div.Price__Label-sc-1g9fitq-1.mVWFG::text').get().encode('ascii','ignore'),
                'ville': annonce.css('div.Card__ContentZone-sc-7insep-3.gfORyM > div.ContentZone__Address-wghbmy-2.fRAjHL > span:nth-child(1)::text').get(),
                'quartier': annonce.css('div.Card__ContentZone-sc-7insep-3.gfORyM > div.ContentZone__Address-wghbmy-2.fRAjHL > span:nth-child(2)::text').get(),
                'lien': annonce.css('div.Card__ContentZone-sc-7insep-3.gfORyM > a::attr(href)').get(),
            }
            
            time.sleep(1)
        
    