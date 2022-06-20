from scrapy import Spider
from scrapy.http.response.html import HtmlResponse
from scrapy.loader import ItemLoader

from AhmedRafik.Items.Cryptocurrency import Cryptocurrency


class CoinMarketCapSpider(Spider):
    name = 'CoinMarketCap'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com/']

    def parse(self, response: HtmlResponse):
        cryptocurrencyUrls = response.xpath("//tbody/tr/td[3]/descendant::a/@href").getall()
        yield from response.follow_all(urls=cryptocurrencyUrls, callback=self.ParseCryptourrency)

    def ParseCryptourrency(self, response: HtmlResponse):
        loader = ItemLoader(item=Cryptocurrency(), response=response)

        loader.add_xpath("Name", "(//h2)[1]/text()")
        loader.add_xpath("image_urls", "//div[contains(@class, 'nameHeader')]/img/@src")
        loader.add_xpath("Price", "//div[@class='priceValue ']/span/text()")
        loader.add_xpath("Rank", "//div[contains(@class, 'namePillPrimary')]/text()")
        loader.add_value("Url", response.url)

        yield loader.load_item()