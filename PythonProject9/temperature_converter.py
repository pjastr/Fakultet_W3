class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        """
        Konwertuje temperaturę z stopni Celsjusza na stopnie Fahrenheita.
        
        Formula: (°C × 9/5) + 32 = °F
        """
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        """
        Konwertuje temperaturę z stopni Fahrenheita na stopnie Celsjusza.
        
        Formula: (°F - 32) × 5/9 = °C
        """
        return (fahrenheit - 32) * 5/9

    def celsius_to_kelvin(self, celsius):
        """
        Konwertuje temperaturę z stopni Celsjusza na Kelwiny.
        
        Formula: °C + 273.15 = K
        
        Rzuca ValueError jeśli wynikowa temperatura jest poniżej zera absolutnego.
        """
        if celsius < -273.15:
            raise ValueError("Temperatura nie może być niższa niż zero absolutne (-273.15°C)")
        return celsius + 273.15

    def kelvin_to_celsius(self, kelvin):
        """
        Konwertuje temperaturę z Kelwinów na stopnie Celsjusza.
        
        Formula: K - 273.15 = °C
        
        Rzuca ValueError jeśli temperatura w Kelwinach jest ujemna.
        """
        if kelvin < 0:
            raise ValueError("Temperatura w Kelwinach nie może być ujemna")
        return kelvin - 273.15