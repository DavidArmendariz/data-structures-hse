import unittest
from ..probability_not_angry import not_angry


class TestProbabilityNotAngry(unittest.TestCase):
    def test_probability_four_days(self):
        self.assertEqual(not_angry(4), 8)