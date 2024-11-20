import pytest
from source.discount_calc import DiscountCalculator

@pytest.fixture()
def base_price():
   return 100

valid_test_data = [(50, 50), (10, 90),(100,0), (20,30)]
invalid_test_data = [-50,120,30]

@pytest.mark.parametrize("discount, final_price", valid_test_data)
def test_discount_valid_cases(base_price, discount, final_price):
    calculated_discount = DiscountCalculator(base_price,discount).calculate_discounted_price()
    assert calculated_discount == final_price

@pytest.mark.parametrize("discount", invalid_test_data)
def test_discount_valid_cases(base_price, discount):
    with pytest.raises(ValueError):
        DiscountCalculator(base_price,discount)



