class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, product, qty):
        if product.stock < qty:
            return False
        self.items.append((product, qty))
        self.total += product.price * qty
        product.stock -= qty
        return True

