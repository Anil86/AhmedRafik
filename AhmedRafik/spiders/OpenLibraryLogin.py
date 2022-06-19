from typing import Dict

from scrapy import Spider
from scrapy.http.response.html import HtmlResponse
from scrapy.http.request.form import FormRequest


class OpenLibraryLoginSpider(Spider):
    name = 'OpenLibraryLogin'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/account/login']

    def parse(self, response: HtmlResponse):
        form = "//form[@id='register']"
        payload: Dict[str, str] = \
            {
                "username": "anil.misc@outlook.com",
                "password": "2E?q3mM^zG*U3N6(",
                "redirect": "",
                "debug_token": "",
                "login": "Log In"
            }
        yield FormRequest.from_response(response=response, formxpath=form, formdata=payload, callback=self.AfterLogin)

    def AfterLogin(self, response: HtmlResponse):
        logOut = response.xpath("//button[text()='Log out']")
        if logOut:
            self.logger.info("Logged in :)")