from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str
    password: str

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int


@dataclass
class Order:
    id: int
    order_item: int
    user_id: int

@dataclass
class OrderItem:
    id: int
    product_id: int
    quantity: int


