# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from itemloaders.processors import TakeFirst
from scrapy import Item, Field


class Cryptocurrency(Item):
    # define the fields for your item here like:
    Name = Field(output_processor=TakeFirst())
    images = Field()
    image_urls = Field()
    Price = Field()
    Rank = Field()
    Url = Field(output_processor=TakeFirst())