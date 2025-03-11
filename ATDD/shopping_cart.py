class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def __hash__(self):
        return hash((self.name, self.price))


class OutOfStockError(Exception):
    """Wyjątek zgłaszany, gdy produkt jest niedostępny w magazynie."""
    pass


class Inventory:
    def __init__(self):
        self.products = {}  # {product: quantity}

    def add_product(self, product, quantity):
        self.products[product] = quantity

    def is_available(self, product, quantity=1):
        """Sprawdza, czy produkt jest dostępny w żądanej ilości."""
        return product in self.products and self.products[product] >= quantity

    def get_available_products(self):
        """Zwraca listę dostępnych produktów (ilość > 0)."""
        return [product for product, quantity in self.products.items() if quantity > 0]

    def remove_from_inventory(self, product, quantity):
        """Zmniejsza dostępną ilość produktu w magazynie."""
        if self.is_available(product, quantity):
            self.products[product] -= quantity
        else:
            raise OutOfStockError(f"Produkt {product.name} nie jest dostępny w żądanej ilości.")


class DiscountCode:
    def __init__(self, code, percentage):
        self.code = code
        self.percentage = percentage


class ShoppingCart:
    def __init__(self, inventory):
        self.inventory = inventory
        self.items = []  # [{"product": product, "quantity": quantity}]
        self.discount_codes = {}  # {code: discount_object}
        self.applied_discount = None

    def add_product(self, product, quantity=1):
        """Dodaje produkt do koszyka."""
        # Sprawdzamy, czy produkt jest dostępny w magazynie
        if not self.inventory.is_available(product, quantity):
            raise OutOfStockError(f"Produkt {product.name} nie jest dostępny w żądanej ilości.")

        # Dodajemy produkt do koszyka
        for item in self.items:
            if item["product"] == product:
                item["quantity"] += quantity
                break
        else:
            self.items.append({"product": product, "quantity": quantity})

        # Zmniejszamy dostępną ilość w magazynie
        self.inventory.remove_from_inventory(product, quantity)

    def remove_product(self, product):
        """Usuwa produkt z koszyka."""
        for i, item in enumerate(self.items):
            if item["product"] == product:
                # Zwracamy produkt do magazynu
                quantity = item["quantity"]
                self.inventory.add_product(product, quantity)

                # Usuwamy produkt z koszyka
                self.items.pop(i)
                break

    def get_items(self):
        """Zwraca listę produktów w koszyku."""
        return self.items

    def get_subtotal(self):
        """Oblicza sumę koszyka przed rabatem."""
        return sum(item["product"].price * item["quantity"] for item in self.items)

    def get_total(self):
        """Oblicza sumę koszyka po rabacie (jeśli jest zastosowany)."""
        subtotal = self.get_subtotal()
        if self.applied_discount:
            discount_amount = subtotal * (self.applied_discount.percentage / 100)
            return subtotal - discount_amount
        return subtotal

    def add_discount_code(self, discount):
        """Dodaje kod rabatowy do systemu."""
        self.discount_codes[discount.code] = discount

    def apply_discount_code(self, code):
        """Stosuje kod rabatowy do koszyka."""
        if code in self.discount_codes:
            self.applied_discount = self.discount_codes[code]
            return True
        return False