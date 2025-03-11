import unittest
from shopping_cart import ShoppingCart, Product


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()
        
        # Przykładowe produkty do testów
        self.product1 = Product("Laptop", 3500.00)
        self.product2 = Product("Mysz", 150.00)
        self.product3 = Product("Klawiatura", 250.00)

    def test_add_product(self):
        # Dodanie jednego produktu
        self.cart.add_product(self.product1, 1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].product.name, "Laptop")
        self.assertEqual(self.cart.items[0].quantity, 1)
        
        # Dodanie drugiego produktu
        self.cart.add_product(self.product2, 2)
        self.assertEqual(len(self.cart.items), 2)
        self.assertEqual(self.cart.items[1].product.name, "Mysz")
        self.assertEqual(self.cart.items[1].quantity, 2)

    def test_add_existing_product(self):
        # Dodanie produktu
        self.cart.add_product(self.product1, 1)
        
        # Dodanie tego samego produktu powinno zwiększyć ilość
        self.cart.add_product(self.product1, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].quantity, 3)

    def test_remove_product(self):
        # Dodanie produktów
        self.cart.add_product(self.product1, 1)
        self.cart.add_product(self.product2, 2)
        
        # Usunięcie produktu
        self.cart.remove_product(self.product1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].product.name, "Mysz")
        
        # Usunięcie nieistniejącego produktu
        with self.assertRaises(ValueError):
            self.cart.remove_product(self.product3)

    def test_update_quantity(self):
        # Dodanie produktu
        self.cart.add_product(self.product1, 1)
        
        # Aktualizacja ilości
        self.cart.update_quantity(self.product1, 5)
        self.assertEqual(self.cart.items[0].quantity, 5)
        
        # Aktualizacja ilości dla nieistniejącego produktu
        with self.assertRaises(ValueError):
            self.cart.update_quantity(self.product3, 3)
            
        # Aktualizacja ilości na wartość niedodatnią
        with self.assertRaises(ValueError):
            self.cart.update_quantity(self.product1, 0)
        
        with self.assertRaises(ValueError):
            self.cart.update_quantity(self.product1, -2)

    def test_get_total(self):
        # Pusty koszyk
        self.assertEqual(self.cart.get_total(), 0)
        
        # Dodanie produktów
        self.cart.add_product(self.product1, 1)  # 3500.00
        self.cart.add_product(self.product2, 2)  # 2 x 150.00 = 300.00
        
        # Sprawdzenie sumy
        self.assertEqual(self.cart.get_total(), 3800.00)

    def test_clear_cart(self):
        # Dodanie produktów
        self.cart.add_product(self.product1, 1)
        self.cart.add_product(self.product2, 2)
        
        # Wyczyszczenie koszyka
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.cart.get_total(), 0)

    def test_apply_discount(self):
        # Dodanie produktów
        self.cart.add_product(self.product1, 1)  # 3500.00
        self.cart.add_product(self.product2, 2)  # 2 x 150.00 = 300.00
        
        # Zastosowanie zniżki procentowej
        self.cart.apply_discount(10)  # 10% zniżki
        self.assertEqual(self.cart.get_total(), 3420.00)  # 3800 - 10% = 3420
        
        # Zastosowanie zniżki kwotowej
        self.cart.apply_fixed_discount(500)
        self.assertEqual(self.cart.get_total(), 2920.00)  # 3420 - 500 = 2920


if __name__ == '__main__':
    unittest.main()