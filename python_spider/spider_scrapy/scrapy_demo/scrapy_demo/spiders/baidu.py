from scrapy import Spider, Request

class TJSpider(Spider):
    name = 'baidu'
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        text = response.text
        print(text)