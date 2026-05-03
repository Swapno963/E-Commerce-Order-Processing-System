from entities.order_item import OrderItem


class OrderItemRepository:
    def __init__(self):
        self.storage = {
            1: OrderItem(id=1, product_id=101, quantity=2),
            2: OrderItem(id=2, product_id=102, quantity=5),
        }

    def get_by_id(self, order_item_id):
        return self.storage.get(order_item_id)

    def save(self, order_item):
        self.storage[order_item.id] = order_item

    def get_all(self):
        return list(self.storage.values())

    def delete(self, order_item_id):
        if order_item_id in self.storage:
            del self.storage[order_item_id]
            return True

        return False
