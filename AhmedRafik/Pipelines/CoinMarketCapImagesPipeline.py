# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.http.request import Request
from scrapy.pipelines.images import ImagesPipeline

from AhmedRafik.Items.Cryptocurrency import Cryptocurrency


class CoinMarketCapImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if not isinstance(item, Cryptocurrency): return None

        adapter = ItemAdapter(item)
        name = adapter["Name"]
        urls = adapter.get("image_urls")
        return {Request(u, cb_kwargs={"imageName": name}) for u in urls}

    def file_path(self, request, response=None, info=None, *, item=None):
        if not isinstance(item, Cryptocurrency): return None

        imageName = request.cb_kwargs["imageName"]
        return f"./full/{imageName}.png"