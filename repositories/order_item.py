
class OrderItemRepository:
    def __init__(self):
        self.storage = {}

    def save(self, order_item):
        self.storage[order_item.id] = order_item

    def get_by_id(self, item_id):
        return self.storage.get(item_id)