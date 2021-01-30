import unittest
from ..lines import lines


class TestLinesProblem(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(lines([2, 2, 1, 1, 1, 2, 1]), 6)

    def test_case_2(self):
        self.assertEqual(lines([0, 0, 0, 0, 0]), 5)

    def test_case_3(self):
        self.assertEqual(lines([2, 3, 1, 4]), 0)