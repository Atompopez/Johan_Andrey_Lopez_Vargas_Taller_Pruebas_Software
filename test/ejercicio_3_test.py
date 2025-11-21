import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'main'))
from shop import Product, ShoppingCart

def test_full_purchase_flow():
    laptop = Product("Laptop", 1000, 10)
    mouse = Product("Mouse", 50, 20)

    cart = ShoppingCart()

    assert cart.add_item(laptop, 1)
    assert cart.add_item(mouse, 2)

    assert cart.total == 1100
    assert laptop.stock == 9
    assert mouse.stock == 18
