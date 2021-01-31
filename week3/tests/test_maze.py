import unittest
import math
from ..maze import (
    fastest_escape_length,
    fastest_escapes,
    weighted_escape_length,
    weighted_escapes,
)

test_a = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
test_b = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]


class TestMaze(unittest.TestCase):
    def test_fastest_escape_length(self):
        self.assertEqual(fastest_escape_length(test_a), 5)

    def test_fastest_escape_length_inf(self):
        self.assertEqual(fastest_escape_length(test_b), math.inf)

    def test_fastest_escapes_case_1(self):
        result = fastest_escapes(test_a)
        self.assertEqual(result, [[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]])

    def test_fastest_escapes_case_2(self):
        self.assertEqual(fastest_escapes(test_b), [])

    def test_fastest_escapes_case_3(self):
        maze = [[0 for _ in range(3)] for _ in range(3)]
        paths = fastest_escapes(maze)
        result = list(map(len, paths))
        self.assertEqual(result, [5, 5, 5, 5, 5, 5])

    def test_weighted_escape_length_case_1(self):
        self.assertEqual(weighted_escape_length(test_a, 0), 2)

    def test_weighted_escape_length_case_2(self):
        self.assertEqual(weighted_escape_length(test_b, 1), 5)

    def test_weighted_escape_length_case_3(self):
        self.assertEqual(weighted_escape_length(test_b, 2), 6)

    def weighted_escape_case_1(self):
        self.assertEqual(
            weighted_escapes(test_b, 0), [[(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]]
        )
