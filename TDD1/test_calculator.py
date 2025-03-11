import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)

        # Testujemy różne przypadki
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)

        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_multiply(self):
        result = self.calc.multiply(2, 5)
        self.assertEqual(result, 10)

        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

        self.assertEqual(self.calc.divide(10, 4), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()