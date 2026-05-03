from abc import ABC, abstractmethod


class OrderServiceInterface(ABC):

    @abstractmethod
    def create_order(self, id, order_item, user_id):
        pass

    @abstractmethod
    def get_order(self, order_id):
        pass

    @abstractmethod
    def get_all_orders(self):
        pass

    @abstractmethod
    def get_orders_by_user(self, user_id):
        pass

    @abstractmethod
    def delete_order(self, order_id):
        pass


class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, price):
        pass
