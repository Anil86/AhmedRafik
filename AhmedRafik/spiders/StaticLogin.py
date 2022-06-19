from scrapy import Spider
from scrapy.http.response.html import HtmlResponse


class StaticLoginSpider(Spider):
    name = 'StaticLogin'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response:HtmlResponse):
        self.logger.info(f"User-Agent: {response.request.headers['User-Agent']}")