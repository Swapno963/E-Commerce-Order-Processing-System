from interfaces.product import ProductService
from entities.product import Product


class ProductRepository:
    def __init__(self):
        self.storage = {
            1: Product(1, "Laptop", 1000.0, 5),
            2: Product(2, "Mouse", 20.0, 50),
        }

    def get_by_id(self, product_id):
        return self.storage.get(product_id)

    def save(self, product):
        self.storage[product.id] = product

    def reduce_stock(self, product_id, quantity):
        product = self.storage.get(product_id)
        if product:
            product.stock -= quantity

    def get_all(self):
        return self.storage
