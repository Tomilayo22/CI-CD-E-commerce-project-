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
