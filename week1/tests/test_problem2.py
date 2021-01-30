import unittest
from ..problem2 import is_palindrome


class TestProblem2(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_palindrome(" mad am    "), True)

    def test_case_2(self):
        self.assertEqual(is_palindrome("  ma d  "), False)