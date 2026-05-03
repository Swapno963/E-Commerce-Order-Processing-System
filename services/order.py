from interfaces.order import OrderServiceInterface
from entities.order import Order


class OrderService(OrderServiceInterface):

    def __init__(self, order_repo):
        self.order_repo = order_repo

    def create_order(self, id, order_item, user_id):

        if user_id <= 0:
            raise Exception("Invalid user_id")

        if order_item <= 0:
            raise Exception("Invalid order_item")

        order = Order(id=id, order_item=order_item, user_id=user_id)

        self.order_repo.save(order)

        return order

    def get_order(self, order_id):
        order = self.order_repo.get_by_id(order_id)

        if not order:
            raise Exception("Order not found")

        return order

    def get_all_orders(self):
        return self.order_repo.get_all()

    def get_orders_by_user(self, user_id):
        return self.order_repo.get_by_user_id(user_id)

    def delete_order(self, order_id):
        deleted = self.order_repo.delete(order_id)

        if not deleted:
            raise Exception("Order not found")

        return "Order deleted successfully"
