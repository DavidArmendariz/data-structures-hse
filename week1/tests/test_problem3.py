import unittest
from ..problem3 import find_unique


class TestProblem3(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_unique([1, 2, 2, 2, 3, 3]), 3)
