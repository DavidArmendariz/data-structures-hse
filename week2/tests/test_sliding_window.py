import unittest
from ..sliding_window_min import sliding_window_min


class TestDeque(unittest.TestCase):
    def test_case_1(self):
        test_a, test_k = [1, 3, 4, 5, 2, 7], 3
        self.assertEqual(sliding_window_min(test_a, test_k), [1, 3, 2, 2])

    def test_case_2(self):
        test_a, test_k = [5, 4, 10, 1], 2
        self.assertEqual(sliding_window_min(test_a, test_k), [4, 4, 1])

    def test_case_3(self):
        test_a, test_k = [10, 20, 6, 10, 8], 5
        self.assertEqual(sliding_window_min(test_a, test_k), [6])
