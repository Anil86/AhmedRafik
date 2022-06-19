from scrapy import Spider
from scrapy.http.request import Request
from scrapy.http.request.form import FormRequest
from scrapy.http.response.html import HtmlResponse


class StaticLoginSpider(Spider):
    name = 'StaticLogin'
    allowed_domains = ['quotes.toscrape.com']

    def start_requests(self):
        yield Request(url="http://quotes.toscrape.com/login", callback=self.Login)

    def Login(self, response: HtmlResponse):
        formXpath = "//form[@action='/login']"
        payload = \
            {
                "csrf_token": response.xpath("//input[@name='csrf_token']/@value").get(),
                "username": "admin",
                "password": "password"
            }
        yield FormRequest.from_response(response=response, formxpath=formXpath, formdata=payload,
                                        callback=self.Parse, clickdata={"value": "Login"})

    def Parse(self, response: HtmlResponse):
        if not self.IsAuthenticated(response):
            self.logger.error("Login failed!!!")
            return

        self.logger.info("Logged in successfully :)")

    def IsAuthenticated(self, response) -> bool:
        logOut = response.xpath("//a[text()='Logout']")
        return True if logOut else False