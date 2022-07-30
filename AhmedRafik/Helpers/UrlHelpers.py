from http.cookies import SimpleCookie


class UrlHelpers:
    @staticmethod
    def ParseCookie(cookiesText: str):
        parser = SimpleCookie()
        parser.load(cookiesText)
        cookieItems = parser.items()
        return dict({k: m.value for k, m in cookieItems})