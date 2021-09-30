from decimal import Decimal, ROUND_UP


def round_to_nearest_multiple_of(number, multiple_of):
    return Decimal(round(number / multiple_of, 2)).quantize(0, rounding=ROUND_UP) * multiple_of
