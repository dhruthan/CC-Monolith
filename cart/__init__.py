import json
from products import Product
from cart import dao
import products

class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> "Cart":
        return Cart(data["id"], data["username"], data["contents"], data["cost"])


def get_cart(username: str) -> list[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []
    all_item_ids = []
    for cart_detail in cart_details:
        all_item_ids.extend(json.loads(cart_detail["contents"]))
    all_products = products.get_products(all_item_ids)  # Batch fetch

    return all_products


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)


def checkout(cart: list[Product]) -> float:
    total_cost = sum(item.cost for item in cart)
    return total_cost
