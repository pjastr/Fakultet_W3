import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        calc = Calculator()
        result = calc.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = self.calc.multiply(2, 5)
        self.assertEqual(result, 10)

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()