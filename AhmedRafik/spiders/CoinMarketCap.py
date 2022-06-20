from scrapy import Spider
from scrapy.http.response.html import HtmlResponse


class CoinMarketCapSpider(Spider):
    name = 'CoinMarketCap'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com/']

    def parse(self, response: HtmlResponse):
        self.logger.info(f"Url: {response.url}")