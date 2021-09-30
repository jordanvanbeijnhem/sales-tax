import re
from decimal import Decimal

from exceptions import InvalidShoppingBasketItemString
from models import ShoppingBasketItem


class ShoppingBasketItemParser:
    ITEM_STRING_PARSING_REGEX = re.compile("(?P<amount>\d+) (?P<description>[a-zA-Z ]*) at (?P<gross_price>\d+\.\d+)")
    TAX_EXEMPTED_ITEM_KEYWORDS = ["book", "chocolate", "headache pills"]
    IMPORTED_ITEM_KEYWORD = "imported"

    @staticmethod
    def parse_shopping_basket_item_string(item_string: str):
        match = ShoppingBasketItemParser.ITEM_STRING_PARSING_REGEX.match(item_string)
        if not match:
            raise InvalidShoppingBasketItemString

        amount = int(match.group("amount"))
        description = match.group("description")
        gross_price = Decimal(match.group("gross_price"))
        exempted_item = any(keyword in description for keyword in ShoppingBasketItemParser.TAX_EXEMPTED_ITEM_KEYWORDS)
        imported_item = ShoppingBasketItemParser.IMPORTED_ITEM_KEYWORD in description
        return ShoppingBasketItem(amount, description, gross_price, exempted_item, imported_item)
