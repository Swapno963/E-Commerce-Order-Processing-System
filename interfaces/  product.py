from abc import ABC, abstractmethod


class ProductService(ABC):

    @abstractmethod
    def addProduct(self, name: str, price: int, stock: int):
        pass

    @abstractmethod
    def viewAllProducts(self):
        pass

    @abstractmethod
    def updateStockProduct(self, id: int, updated_stock: int):
        pass
