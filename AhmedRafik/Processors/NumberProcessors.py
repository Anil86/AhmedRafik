from price_parser import Price


class NumberProcessors:
    @staticmethod
    def ParsePrice(priceStr: str) -> float:
        price = Price.fromstring(priceStr, currency_hint='$')
        return price.amount_float

    @staticmethod
    def ParseCryptocurrencyRank(rank: str) -> int:
        return int(rank[6:])