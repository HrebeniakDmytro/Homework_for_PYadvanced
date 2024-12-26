import unittest
from task2 import *

class TestBMICalculation(unittest.TestCase):
    def test_normal_weight(self):
        self.assertEqual(calculate_bmi(1.8, 70), "Маса тіла в нормі")

    def test_underweight(self):
        self.assertEqual(calculate_bmi(1.6, 45), "Недостатня вага")

    def test_overweight(self):
        self.assertEqual(calculate_bmi(1.7, 85), "Слідкуйте за фігурою")

    def test_invalid_height_zero(self):
        with self.assertRaises(ValueError):
            calculate_bmi(0, 70)

    def test_invalid_weight_negative(self):
        with self.assertRaises(ValueError):
            calculate_bmi(1.8, -10)

    def test_boundary_underweight(self):
        self.assertEqual(calculate_bmi(1.8, 59.94), "Недостатня вага")

    def test_boundary_normal(self):
        self.assertEqual(calculate_bmi(1.8, 80.99), "Маса тіла в нормі")

if __name__ == "__main__":
    unittest.main()
