from interfaces.order import DiscountStrategy


class VIPDiscount(DiscountStrategy):

    def apply_discount(self, price):
        return price * 0.8


class EidDiscount(DiscountStrategy):

    def apply_discount(self, price):
        return price * 0.7
