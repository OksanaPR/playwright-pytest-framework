import pytest

from utils.math_utils import discount


# @pytest.mark.parametrize (
#     "percent, expected",
#     [
#         (10, 90),
#         (0, 100),
#         (100, 0)
#     ]
# )
# def test_discount(default_price, percent, expected):
#     result = discount(default_price, percent)
#     assert result == expected
#
#
# @pytest.mark.parametrize(
#     "percent",
#     [
#         150,
#         -5,
#         200
#     ]
# )
# def test_discount_invalid_percentage(default_price, percent):
#     with pytest.raises(ValueError,  match="Discount must be between 0 and 100"):
#         discount(default_price, percent)
#
# def test_discount_using_fixture(default_price, standard_discount):
#     assert discount(default_price, standard_discount) == 90
#
# def test_expensive_price(expensive_price, standard_discount):
#     assert discount(expensive_price, standard_discount) == 450
#
# def test_vip_discount(default_price, vip_discount):
#     assert discount(default_price, vip_discount) == 75

def test_sample_list(sample_list):
    sample_list.append("Book")
    assert len(sample_list) == 1

def test_empty_list(sample_list):
    assert len(sample_list) == 0