import re


class EmailValidator:
    def __init__(self, allowed_domains=None):
        """
        Inicjalizuje walidator adresów email.
        
        Parametry:
        allowed_domains (list): Opcjonalna lista dozwolonych domen.
                               Jeśli podana, tylko adresy z tych domen będą uznane za prawidłowe.
        """
        self.allowed_domains = allowed_domains
        # Prosty wzorzec regex do walidacji adresów email
        self.pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    def is_valid(self, email):
        """
        Sprawdza, czy podany adres email jest prawidłowy.
        
        Parametry:
        email (str): Adres email do sprawdzenia
        
        Zwraca:
        bool: True jeśli adres jest prawidłowy, False w przeciwnym przypadku
        """
        if email is None:
            return False
            
        if not isinstance(email, str):
            return False
            
        # Sprawdzenie podstawowego formatu emaila
        if not re.match(self.pattern, email):
            return False
            
        # Jeśli określono dozwolone domeny, sprawdź czy email ma jedną z nich
        if self.allowed_domains:
            domain = email.split('@')[1]
            if domain not in self.allowed_domains:
                return False
                
        return True

    def normalize(self, email):
        """
        Normalizuje adres email przez usunięcie białych znaków i zamianę na małe litery.
        
        Parametry:
        email (str): Adres email do normalizacji
        
        Zwraca:
        str: Znormalizowany adres email
        """
        if email is None:
            return None
            
        return email.strip().lower()