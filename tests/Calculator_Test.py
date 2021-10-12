import unittest

import pytest

from main.Calculator import Calculator


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive(self):
        self.assertEqual(self.calculator.add(3, 6), 9)

    def test_subtract_positive(self):
        self.assertEqual(self.calculator.subtract(5, 2), 3)

    def test_multiply_positive(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_divide_positive(self):
        self.assertEqual(self.calculator.divide(20, 4), 5)

    def test_add_negative(self):
        self.assertNotEqual(self.calculator.add(2, 6), 9)

    def test_subtract_negative(self):
        self.assertNotEqual(self.calculator.subtract(5, 2), 13)

    def test_multiply_negative(self):
        self.assertNotEqual(self.calculator.multiply(2, 3), 15)

    def test_divide_with_zero_negative(self):
        self.assertEqual(self.calculator.divide(20, 0), "can not divide by zero")


if __name__ == "__main__":
    unittest.main()
