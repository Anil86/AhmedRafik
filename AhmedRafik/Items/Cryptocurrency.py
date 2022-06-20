# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from itemloaders.processors import TakeFirst, MapCompose
from scrapy import Item, Field

from AhmedRafik.Processors.NumberProcessors import NumberProcessors


class Cryptocurrency(Item):
    # define the fields for your item here like:
    Name = Field(output_processor=TakeFirst())
    images = Field()
    image_urls = Field()
    Price = Field(input_processor=MapCompose(NumberProcessors.ParsePrice), output_processor=TakeFirst())
    Rank = Field(input_processor=MapCompose(NumberProcessors.ParseCryptocurrencyRank), output_processor=TakeFirst())
    Url = Field(output_processor=TakeFirst())