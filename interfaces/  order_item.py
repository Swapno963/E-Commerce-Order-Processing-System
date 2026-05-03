from dataclasses import dataclass


@dataclass
class OrderItem:
    id: int
    product_id: int
    quantity: int


