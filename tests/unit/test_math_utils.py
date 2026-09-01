import pytest

from utils.math_utils import discount


@pytest.mark.parametrize (
    "price, percent, expected",
    [
        (100, 10, 90),
        (100, 0, 100),
        (100, 100, 0),
        (200, 25, 150)
    ]
)
def test_discount(price, percent, expected):
    result = discount(price, percent)
    assert result == expected


@pytest.mark.parametrize(
    "price, percent",
    [
        (100, 150),
        (200, -5),
        (101, 200)
    ]
)
def test_discount_invalid_percentage(price, percent):
    with pytest.raises(ValueError,  match="Discount must be between 0 and 100"):
        discount(price, percent)