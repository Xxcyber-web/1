import pytest
from discount import apply_discount

@pytest.mark.parametrize("price, percent, expected", [
    (100, 0, 100),        # No discount
    (100, 50, 50),        # half price
    (100, 100, 0),        # Free
    (200, 25, 150),       # 25% discount
    (80, 10, 72),         # 10% discount 80 = 72
])

def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected