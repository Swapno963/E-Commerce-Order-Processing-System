from entities.order import Order


class OrderRepository:
    def __init__(self):
        self.storage = {
            1: Order(id=1, order_item=1, user_id=1),
            2: Order(id=2, order_item=2, user_id=2),
        }

    def get_by_id(self, order_id):
        return self.storage.get(order_id)

    def save(self, order):
        self.storage[order.id] = order

    def get_all(self):
        return list(self.storage.values())

    def get_by_user_id(self, user_id):
        return [order for order in self.storage.values() if order.user_id == user_id]

    def delete(self, order_id):
        if order_id in self.storage:
            del self.storage[order_id]
            return True
        return False
