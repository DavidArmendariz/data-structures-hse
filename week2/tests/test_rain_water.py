import unittest
from ..rain_water import calc_rain_water


class TestRainWater(unittest.TestCase):
    def test_case_1(self):
        test_h = [2, 5, 2, 3, 6, 9, 1, 3, 4, 6, 1]
        self.assertEqual(calc_rain_water(test_h), 15)

    def test_case_2(self):
        test_h = [2, 4, 6, 8, 6, 4, 2]
        self.assertEqual(calc_rain_water(test_h), 0)

    def test_case_3(self):
        test_h = [8, 6, 4, 2, 4, 6, 8]
        self.assertEqual(calc_rain_water(test_h), 18)
