import random

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

from AhmedRafik.spiders.Quotes import QuotesSpider


class RandomUserAgentMiddleware(UserAgentMiddleware):
    _userAgents = [f"User Agent {i}" for i in range(1, 11)]

    def process_request(self, request, spider):
        if not isinstance(spider, QuotesSpider): return None

        self.user_agent = random.choice(self._userAgents)
        request.headers["User-Agent"] = self.user_agent