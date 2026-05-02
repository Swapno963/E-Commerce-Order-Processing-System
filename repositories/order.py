from main import Order

class OrderRepository:
    def __init__(self):
        self.storage = {}

    def save(self, order):
        self.storage[order.id] = order

    def get_by_id(self, order_id):
        return self.storage.get(order_id)