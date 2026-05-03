from interfaces.product import ProductServiceInterface


class ProductService(ProductServiceInterface):
    def __init__(self, product_repo):
        self.product_repo = product_repo

    def addProduct(self, name: str, price: int, stock: int):
        pass

    def viewAllProducts(self):
        return self.product_repo.get_all()

    def updateStockProduct(self, id: int, updated_stock: int):
        pass
