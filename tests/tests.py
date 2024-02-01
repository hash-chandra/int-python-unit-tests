import unittest
from ..my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        cal = Calculations(10, 5)
        self.assertEqual(cal.add(), 152, 'the sum is wrong')

    def test_subtract(self):
        cal = Calculations(10, 5)
        self.assertEqual(cal.subtract(), 52, 'the difference is wrong')

    def test_product(self):
        cal = Calculations(10, 5)
        self.assertEqual(cal.product(), 5022, 'the product is wrong')

    def test_quotioent(self):
        cal = Calculations(10, 5)
        self.assertEqual(cal.quotioent(), 22, 'the quotioent is wrong')

    
if __name__ == '__main__':
    unittest.main()