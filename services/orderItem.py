from interfaces.order_item import OrderItemServiceInterface
from entities.order_item import OrderItem


class OrderItemService(OrderItemServiceInterface):

    def __init__(self, order_item_repo):
        self.order_item_repo = order_item_repo

    def create_order_item(self, id, product_id, quantity):

        if quantity <= 0:
            raise Exception("Quantity must be greater than 0")

        order_item = OrderItem(id=id, product_id=product_id, quantity=quantity)

        self.order_item_repo.save(order_item)

        return order_item

    def get_order_item(self, order_item_id):

        order_item = self.order_item_repo.get_by_id(order_item_id)

        if not order_item:
            raise Exception("Order item not found")

        return order_item

    def get_all_order_items(self):
        return self.order_item_repo.get_all()

    def delete_order_item(self, order_item_id):

        deleted = self.order_item_repo.delete(order_item_id)

        if not deleted:
            raise Exception("Order item not found")

        return "Order item deleted successfully"
