# Define your e-commerce components

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity

    def remove_item(self, product_id, quantity):
        if product_id in self.items:
            if self.items[product_id] >= quantity:
                self.items[product_id] -= quantity
            else:
                del self.items[product_id]

    def get_cart_total(self):
        total = 0
        # Calculate the total cost based on the items and their prices
        return total

class ProductCatalog:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price):
        self.products[product_id] = {"name": name, "price": price}

    def get_product_info(self, product_id):
        if product_id in self.products:
            return self.products[product_id]
        else:
            return None

# Now, let's write unit tests for these components

import unittest

class TestECommerceComponents(unittest.TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart()
        self.product_catalog = ProductCatalog()

    def test_add_item_to_cart(self):
        self.shopping_cart.add_item("product1", 2)
        self.assertEqual(self.shopping_cart.items["product1"], 2)

    def test_remove_item_from_cart(self):
        self.shopping_cart.add_item("product2", 3)
        self.shopping_cart.remove_item("product2", 1)
        self.assertEqual(self.shopping_cart.items["product2"], 2)

    def test_get_cart_total(self):
        self.product_catalog.add_product("product3", "Item A", 10.0)
        self.product_catalog.add_product("product4", "Item B", 15.0)
        self.shopping_cart.add_item("product3", 2)
        self.shopping_cart.add_item("product4", 1)
        total = self.shopping_cart.get_cart_total()
        self.assertEqual(total, 35.0)

if __name__ == '__main__':
    unittest.main()
