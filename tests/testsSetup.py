import unittest
from ..my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    def setUp(self) -> None:
        self.calculation = Calculations(10, 5)
    
    def test_sum(self):
        self.assertEqual(self.calculation.add(), 15, 'the sum is wrong')

    def test_subtract(self):
        self.assertEqual(self.calculation.subtract(), 5, 'the difference is wrong')

    def test_product(self):
        self.assertEqual(self.calculation.product(), 50, 'the product is wrong')

    def test_quotioent(self):
        self.assertEqual(self.calculation.quotioent(), 2, 'the quotioent is wrong')

    
if __name__ == '__main__':
    unittest.main()