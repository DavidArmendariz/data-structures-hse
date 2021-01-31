import unittest
from ..subsets import subsets


class TestSubsets(unittest.TestCase):
    def test_empty_elements(self):
        self.assertEqual(subsets([]), [[]])

    def test_set_with_one_element(self):
        self.assertEqual(subsets([1]), [[], [1]])