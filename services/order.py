from main import Order, OrderItem

class OrderService:
    def __init__(self, product_repo, order_repo, order_item_repo):
        self.product_repo = product_repo
        self.order_repo = order_repo
        self.order_item_repo = order_item_repo

    def place_order(self, order_id, user_id, product_id, quantity):

        # 1. Fetch product
        product = self.product_repo.get_by_id(product_id)

        if not product:
            raise Exception("Product not found")

        # 2. Stock validation (business rule)
        if product.stock < quantity:
            raise Exception("Insufficient stock")

        # 3. Create OrderItem
        order_item = OrderItem(
            id=order_id,
            product_id=product_id,
            quantity=quantity
        )

        self.order_item_repo.save(order_item)

        # 4. Create Order
        order = Order(
            id=order_id,
            order_item_id=order_item.id,
            user_id=user_id
        )

        self.order_repo.save(order)

        # 5. Update stock
        self.product_repo.reduce_stock(product_id, quantity)

        return order