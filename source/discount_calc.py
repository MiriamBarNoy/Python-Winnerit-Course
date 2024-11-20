class DiscountCalculator:
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount

    #price getter
    @property
    def price(self):
        return self._price

    # discount getter
    @property
    def discount(self):
        return self._discount

    #discount setter
    @discount.setter
    def discount(self, discount_value):
        if 0 < discount_value < 100:
           self._discount = discount_value
        else:
            raise ValueError("Discount must be between 0 and 100")


    #price setter
    def set_price(self, price_value):
        if price_value > 0:
            self._price = price_value
        else:
            raise ValueError("Price must be positive value")

    #calculator
    def calculate_discounted_price(self):
        final_price = (1 - (self._discount / 100)) * self._price
        return final_price

    @price.setter
    def price(self, value):
        self._price = value


#try_usage
# new_price = DiscountCalculator(200, 20).calculate_discounted_price()
# print(new_price)
#
# try_bbb = DiscountCalculator(200,-20).calculate_discounted_price()
# print(try_bbb)
