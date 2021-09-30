from decimal import Decimal

from utils import round_to_nearest_multiple_of


class ShoppingBasketItem:
    BASIC_SALES_TAX_PERCENTAGE = 10
    IMPORT_DUTY_TAX_PERCENTAGE = 5
    ROUND_TAX_TO_MULTIPLE_OF = Decimal(0.05)

    def __init__(self, amount: int, description: str, gross_price: Decimal, exempted_item: bool, imported_item: bool):
        self.amount = amount
        self.description = description
        self.gross_price = gross_price
        self.exempted_item = exempted_item
        self.imported_item = imported_item
        self.tax_percentage = self.calculate_tax_percentage()
        self.sales_tax = round_to_nearest_multiple_of(gross_price * self.tax_percentage / 100,
                                                      self.ROUND_TAX_TO_MULTIPLE_OF)
        self.net_price = self.gross_price + self.sales_tax

    def calculate_tax_percentage(self):
        tax_percentage = 0
        if not self.exempted_item:
            tax_percentage += self.BASIC_SALES_TAX_PERCENTAGE
        if self.imported_item:
            tax_percentage += self.IMPORT_DUTY_TAX_PERCENTAGE
        return tax_percentage


class ShoppingBasket:
    def __init__(self):
        self.items = []

    def add_item(self, item: ShoppingBasketItem):
        self.items.append(item)

    def clear_basket(self):
        self.items = []

    def get_receipt(self):
        total_sales_taxes, total_price = self.calculate_totals()
        receipt_lines = [f"{item.amount} {item.description}: {item.net_price:.2f}" for item in self.items]
        receipt_lines.append(f"Sales Taxes: {total_sales_taxes:.2f}")
        receipt_lines.append(f"Total: {total_price:.2f}")
        return "\n".join(receipt_lines)

    def calculate_totals(self):
        total_sales_taxes = Decimal(0)
        total_price = Decimal(0)
        for item in self.items:
            total_sales_taxes += item.sales_tax
            total_price += item.net_price
        return total_sales_taxes, total_price
