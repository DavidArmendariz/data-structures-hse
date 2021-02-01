import unittest
from ..coins import coins


class TestBoxes(unittest.TestCase):
    def test_coins(self):
        self.assertEqual(coins(13), 3)