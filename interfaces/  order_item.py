from abc import ABC, abstractmethod


class OrderItemServiceInterface(ABC):

    @abstractmethod
    def create_order_item(self, id, product_id, quantity):
        pass

    @abstractmethod
    def get_order_item(self, order_item_id):
        pass

    @abstractmethod
    def get_all_order_items(self):
        pass

    @abstractmethod
    def delete_order_item(self, order_item_id):
        pass
