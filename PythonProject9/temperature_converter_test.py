import unittest
from temperature_converter import TemperatureConverter


class TestTemperatureConverter(unittest.TestCase):

    def setUp(self):
        self.converter = TemperatureConverter()

    def test_celsius_to_fahrenheit(self):
        # Test standardowego przypadku
        result = self.converter.celsius_to_fahrenheit(0)
        self.assertEqual(result, 32)
        
        # Test wartości ujemnej
        result = self.converter.celsius_to_fahrenheit(-40)
        self.assertEqual(result, -40)
        
        # Test dla wody wrzącej
        result = self.converter.celsius_to_fahrenheit(100)
        self.assertEqual(result, 212)

    def test_fahrenheit_to_celsius(self):
        # Test standardowego przypadku
        result = self.converter.fahrenheit_to_celsius(32)
        self.assertEqual(result, 0)
        
        # Test wartości ujemnej
        result = self.converter.fahrenheit_to_celsius(-40)
        self.assertEqual(result, -40)
        
        # Test dla wody wrzącej
        result = self.converter.fahrenheit_to_celsius(212)
        self.assertEqual(result, 100)

    def test_celsius_to_kelvin(self):
        # Test zera absolutnego
        result = self.converter.celsius_to_kelvin(-273.15)
        self.assertAlmostEqual(result, 0, places=2)
        
        # Test dla zera Celsjusza
        result = self.converter.celsius_to_kelvin(0)
        self.assertEqual(result, 273.15)
        
        # Test dla wody wrzącej
        result = self.converter.celsius_to_kelvin(100)
        self.assertEqual(result, 373.15)

    def test_kelvin_to_celsius(self):
        # Test zera absolutnego
        result = self.converter.kelvin_to_celsius(0)
        self.assertAlmostEqual(result, -273.15, places=2)
        
        # Test dla zera Celsjusza
        result = self.converter.kelvin_to_celsius(273.15)
        self.assertEqual(result, 0)
        
        # Test dla wody wrzącej
        result = self.converter.kelvin_to_celsius(373.15)
        self.assertEqual(result, 100)

    def test_invalid_temperature(self):
        # Test dla temperatur poniżej zera absolutnego
        with self.assertRaises(ValueError):
            self.converter.kelvin_to_celsius(-1)
            
        with self.assertRaises(ValueError):
            self.converter.celsius_to_kelvin(-274)


if __name__ == '__main__':
    unittest.main()