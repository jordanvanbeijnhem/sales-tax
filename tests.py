import unittest

from models import ShoppingBasket
from parsers import ShoppingBasketItemParser

INPUT_1 = [
    "1 book at 12.49",
    "1 music CD at 14.99",
    "1 chocolate bar at 0.85",
]
OUTPUT_1 = """1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83"""

INPUT_2 = [
    "1 imported box of chocolates at 10.00",
    "1 imported bottle of perfume at 47.50"
]
OUTPUT_2 = """1 imported box of chocolates: 10.50
1 imported bottle of perfume: 54.65
Sales Taxes: 7.65
Total: 65.15"""

INPUT_3 = [
    "1 imported bottle of perfume at 27.99",
    "1 bottle of perfume at 18.99",
    "1 packet of headache pills at 9.75",
    "1 imported box of chocolates at 11.25",
]
OUTPUT_3 = """1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
1 imported box of chocolates: 11.85
Sales Taxes: 6.70
Total: 74.68"""


class TestInputCases(unittest.TestCase):

    def setUp(self):
        self.shopping_basket = ShoppingBasket()

    def test_input_1(self):
        for input_item in INPUT_1:
            self.shopping_basket.add_item(ShoppingBasketItemParser.parse_shopping_basket_item_string(input_item))
        self.assertEqual(self.shopping_basket.get_receipt(), OUTPUT_1)

    def test_input_2(self):
        for input_item in INPUT_2:
            self.shopping_basket.add_item(ShoppingBasketItemParser.parse_shopping_basket_item_string(input_item))
        self.assertEqual(self.shopping_basket.get_receipt(), OUTPUT_2)

    def test_input_3(self):
        for input_item in INPUT_3:
            self.shopping_basket.add_item(ShoppingBasketItemParser.parse_shopping_basket_item_string(input_item))
        self.assertEqual(self.shopping_basket.get_receipt(), OUTPUT_3)
