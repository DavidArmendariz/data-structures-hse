import unittest
from ..problem1 import find_numbers


class TestProblem1(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_numbers([1, 2, 8, 10, 11], 10), True)