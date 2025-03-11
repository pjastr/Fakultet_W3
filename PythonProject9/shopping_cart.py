class Product:
    def __init__(self, name, price):
        """
        Inicjalizuje nowy produkt.
        
        Parametry:
        name (str): Nazwa produktu
        price (float): Cena produktu
        """
        self.name = name
        self.price = price
        
    def __eq__(self, other):
        """
        Porównuje dwa produkty na podstawie ich nazw.
        """
        if not isinstance(other, Product):
            return False
        return self.name == other.name


class CartItem:
    def __init__(self, product, quantity):
        """
        Inicjalizuje nowy element koszyka.
        
        Parametry:
        product (Product): Produkt
        quantity (int): Ilość produktu
        """
        self.product = product
        self.quantity = quantity
        
    def get_total_price(self):
        """
        Oblicza łączną cenę dla elementu koszyka.
        
        Zwraca:
        float: Łączna cena (ilość * cena jednostkowa)
        """
        return self.product.price * self.quantity


class ShoppingCart:
    def __init__(self):
        """
        Inicjalizuje nowy koszyk zakupowy.
        """
        self.items = []
        self.percentage_discount = 0
        self.fixed_discount = 0
        
    def add_product(self, product, quantity):
        """
        Dodaje produkt do koszyka lub zwiększa jego ilość jeśli już istnieje.
        
        Parametry:
        product (Product): Produkt do dodania
        quantity (int): Ilość produktu do dodania
        """
        for item in self.items:
            if item.product == product:
                item.quantity += quantity
                return
                
        self.items.append(CartItem(product, quantity))
        
    def remove_product(self, product):
        """
        Usuwa produkt z koszyka.
        
        Parametry:
        product (Product): Produkt do usunięcia
        
        Rzuca:
        ValueError: Jeśli produkt nie istnieje w koszyku
        """
        for i, item in enumerate(self.items):
            if item.product == product:
                self.items.pop(i)
                return
                
        raise ValueError(f"Produkt {product.name} nie istnieje w koszyku")
        
    def update_quantity(self, product, quantity):
        """
        Aktualizuje ilość produktu w koszyku.
        
        Parametry:
        product (Product): Produkt do zaktualizowania
        quantity (int): Nowa ilość produktu
        
        Rzuca:
        ValueError: Jeśli produkt nie istnieje w koszyku lub ilość jest niedodatnia
        """
        if quantity <= 0:
            raise ValueError("Ilość musi być dodatnia")
            
        for item in self.items:
            if item.product == product:
                item.quantity = quantity
                return
                
        raise ValueError(f"Produkt {product.name} nie istnieje w koszyku")
        
    def get_total(self):
        """
        Oblicza łączną cenę koszyka z uwzględnieniem zniżek.
        
        Zwraca:
        float: Łączna cena koszyka
        """
        total = sum(item.get_total_price() for item in self.items)
        
        # Zastosowanie zniżki procentowej
        if self.percentage_discount > 0:
            discount_amount = total * (self.percentage_discount / 100)
            total -= discount_amount
            
        # Zastosowanie zniżki kwotowej
        total = max(0, total - self.fixed_discount)
        
        return total
        
    def clear(self):
        """
        Czyści koszyk, usuwając wszystkie produkty.
        """
        self.items = []
        self.percentage_discount = 0
        self.fixed_discount = 0
        
    def apply_discount(self, percentage):
        """
        Stosuje zniżkę procentową do koszyka.
        
        Parametry:
        percentage (float): Wartość zniżki w procentach (np. 10 dla 10%)
        """
        self.percentage_discount = percentage
        
    def apply_fixed_discount(self, amount):
        """
        Stosuje zniżkę kwotową do koszyka.
        
        Parametry:
        amount (float): Wartość zniżki w walucie
        """
        self.fixed_discount = amount