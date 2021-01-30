import unittest
from ..largest_palindrome import largest_palindrome


class TestLargestPalindrome(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(largest_palindrome("ABBCB"), "BCB")

    def test_case_2(self):
        self.assertEqual(largest_palindrome("ABACABAD"), "ABACABA")

    def test_case_3(self):
        self.assertEqual(largest_palindrome("ABCDE"), "A")