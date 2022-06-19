from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from AhmedRafik.spiders.StaticLogin import StaticLoginSpider


class Program:
    @staticmethod
    def Main():
        crawler = CrawlerProcess(settings=get_project_settings())
        crawler.crawl(StaticLoginSpider)
        crawler.start()


if __name__ == "__main__": Program.Main()