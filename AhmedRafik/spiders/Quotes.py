from itemloaders.processors import TakeFirst
from scrapy import Spider
from scrapy.http.response.html import HtmlResponse
from scrapy.loader import ItemLoader

from AhmedRafik.Items.Quote import Quote


class QuotesSpider(Spider):
    name = 'Quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response: HtmlResponse):
        self.logger.info(f"Random User Agent: {response.request.headers['User-Agent']}")

        quotes = response.xpath("//span[@class='text']/text()").getall()
        for quote in quotes:
            loader = ItemLoader(Quote())
            loader.default_output_processor = TakeFirst()

            loader.add_value("Text", quote)

            yield loader.load_item()

        nextPage = response.xpath("//a[starts-with(text(), 'Next')]/@href").get()
        if nextPage is not None:
            yield response.follow(nextPage)