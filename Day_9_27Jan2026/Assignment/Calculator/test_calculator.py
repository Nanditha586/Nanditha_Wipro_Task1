import unittest
from calculator import addition, subtraction, multiplication, division
class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2,2), 4)
    def test_subtraction(self):
        self.assertEqual(subtraction(2,2), 0)
    def test_multiplication(self):
        self.assertEqual(multiplication(2,2), 4)
    def test_division(self):
        self.assertEqual(division(2,2), 1.0)
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(2,0)
if __name__ == "__main__":
    unittest.main()