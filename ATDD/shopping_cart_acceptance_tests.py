import unittest
from shopping_cart import ShoppingCart, Product, Inventory, DiscountCode, OutOfStockError


class ShoppingCartAcceptanceTests(unittest.TestCase):
    """
    Testy akceptacyjne dla funkcjonalności koszyka zakupowego.
    """

    def setUp(self):
        """Przygotowanie środowiska testowego."""
        # Tworzymy magazyn i dodajemy do niego produkty
        self.inventory = Inventory()

        # Produkt dostępny w magazynie (10 sztuk)
        self.laptop = Product("Laptop", 3500.00)
        self.inventory.add_product(self.laptop, 10)

        # Produkt dostępny w magazynie (5 sztuk)
        self.headphones = Product("Słuchawki", 200.00)
        self.inventory.add_product(self.headphones, 5)

        # Produkt niedostępny w magazynie (0 sztuk)
        self.smartphone = Product("Smartfon", 2000.00)
        self.inventory.add_product(self.smartphone, 0)

        # Tworzymy koszyk zakupowy powiązany z magazynem
        self.cart = ShoppingCart(self.inventory)

        # Dodajemy kody rabatowe do systemu
        self.discount_code = DiscountCode("RABAT10", 10)  # 10% rabatu
        self.cart.add_discount_code(self.discount_code)

    def test_customer_can_add_products_to_cart(self):
        """
        Kryterium akceptacji 1: Klient może dodawać produkty do koszyka.
        """
        # Dodajemy produkty do koszyka
        self.cart.add_product(self.laptop, 1)
        self.cart.add_product(self.headphones, 2)

        # Sprawdzamy, czy produkty zostały dodane do koszyka
        cart_items = self.cart.get_items()

        # Weryfikujemy, że koszyk zawiera dwa rodzaje produktów
        self.assertEqual(len(cart_items), 2)

        # Weryfikujemy, że koszyk zawiera laptop (1 sztuka)
        self.assertEqual(cart_items[0]["product"], self.laptop)
        self.assertEqual(cart_items[0]["quantity"], 1)

        # Weryfikujemy, że koszyk zawiera słuchawki (2 sztuki)
        self.assertEqual(cart_items[1]["product"], self.headphones)
        self.assertEqual(cart_items[1]["quantity"], 2)

    def test_customer_can_remove_products_from_cart(self):
        """
        Kryterium akceptacji 2: Klient może usuwać produkty z koszyka.
        """
        # Najpierw dodajemy produkty do koszyka
        self.cart.add_product(self.laptop, 1)
        self.cart.add_product(self.headphones, 2)

        # Sprawdzamy, czy koszyk zawiera dwa rodzaje produktów
        self.assertEqual(len(self.cart.get_items()), 2)

        # Usuwamy laptop z koszyka
        self.cart.remove_product(self.laptop)

        # Weryfikujemy, że koszyk zawiera tylko jeden rodzaj produktu
        cart_items = self.cart.get_items()
        self.assertEqual(len(cart_items), 1)

        # Weryfikujemy, że w koszyku pozostały tylko słuchawki
        self.assertEqual(cart_items[0]["product"], self.headphones)
        self.assertEqual(cart_items[0]["quantity"], 2)

    def test_customer_can_see_cart_total(self):
        """
        Kryterium akceptacji 3: Klient może zobaczyć sumę wszystkich produktów w koszyku.
        """
        # Dodajemy produkty do koszyka
        self.cart.add_product(self.laptop, 1)  # 1 x 3500.00 = 3500.00
        self.cart.add_product(self.headphones, 2)  # 2 x 200.00 = 400.00
        # Oczekiwana suma: 3900.00

        # Weryfikujemy, że suma koszyka jest poprawna
        self.assertEqual(self.cart.get_total(), 3900.00)

    def test_customer_can_apply_discount_code(self):
        """
        Kryterium akceptacji 4: Klient może zastosować kod rabatowy, który obniży cenę o określony procent.
        """
        # Dodajemy produkty do koszyka
        self.cart.add_product(self.laptop, 1)  # 1 x 3500.00 = 3500.00
        self.cart.add_product(self.headphones, 2)  # 2 x 200.00 = 400.00
        # Suma przed rabatem: 3900.00

        # Sprawdzamy sumę przed zastosowaniem rabatu
        self.assertEqual(self.cart.get_total(), 3900.00)

        # Stosujemy kod rabatowy (10%)
        self.cart.apply_discount_code("RABAT10")

        # Oczekiwana suma po rabacie: 3900.00 - 10% = 3510.00
        self.assertEqual(self.cart.get_total(), 3510.00)

    def test_cart_verifies_product_availability(self):
        """
        Kryterium akceptacji 5: System powinien weryfikować, czy produkt jest dostępny w magazynie przed dodaniem do koszyka.
        """
        # Próbujemy dodać do koszyka produkt, którego nie ma w magazynie
        with self.assertRaises(OutOfStockError):
            self.cart.add_product(self.smartphone, 1)

        # Weryfikujemy, że koszyk jest pusty (produkt nie został dodany)
        self.assertEqual(len(self.cart.get_items()), 0)

    def test_cart_verifies_quantity_availability(self):
        """
        Rozszerzenie kryterium akceptacji 5: System powinien weryfikować, czy ilość produktu jest dostępna w magazynie.
        """
        # Próbujemy dodać więcej słuchawek niż jest dostępnych w magazynie (dostępne: 5)
        with self.assertRaises(OutOfStockError):
            self.cart.add_product(self.headphones, 6)

        # Weryfikujemy, że koszyk jest pusty (produkt nie został dodany)
        self.assertEqual(len(self.cart.get_items()), 0)

        # Dodajemy dopuszczalną ilość słuchawek
        self.cart.add_product(self.headphones, 5)

        # Weryfikujemy, że słuchawki zostały dodane do koszyka
        cart_items = self.cart.get_items()
        self.assertEqual(len(cart_items), 1)
        self.assertEqual(cart_items[0]["product"], self.headphones)
        self.assertEqual(cart_items[0]["quantity"], 5)

    def test_end_to_end_customer_shopping_flow(self):
        """
        Test akceptacyjny dla pełnego przepływu zakupowego (scenariusz end-to-end).
        """
        # 1. Klient przegląda dostępne produkty
        available_products = self.inventory.get_available_products()
        self.assertIn(self.laptop, available_products)
        self.assertIn(self.headphones, available_products)
        self.assertNotIn(self.smartphone, available_products)  # Niedostępny (0 sztuk)

        # 2. Klient dodaje produkty do koszyka
        self.cart.add_product(self.laptop, 1)
        self.cart.add_product(self.headphones, 3)

        # 3. Klient sprawdza zawartość koszyka
        cart_items = self.cart.get_items()
        self.assertEqual(len(cart_items), 2)

        # 4. Klient usuwa jeden z produktów
        self.cart.remove_product(self.laptop)
        cart_items = self.cart.get_items()
        self.assertEqual(len(cart_items), 1)

        # 5. Klient sprawdza sumę koszyka
        # 3 x 200.00 = 600.00
        self.assertEqual(self.cart.get_total(), 600.00)

        # 6. Klient stosuje kod rabatowy
        self.cart.apply_discount_code("RABAT10")

        # 7. Klient sprawdza sumę po rabacie
        # 600.00 - 10% = 540.00
        self.assertEqual(self.cart.get_total(), 540.00)


if __name__ == '__main__':
    unittest.main()