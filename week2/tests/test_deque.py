import unittest
from ..deque import process_deque


class TestDeque(unittest.TestCase):
    def test_case_1(self):
        test_cmd = [
            "push_front 1",
            "push_front 2",
            "push_back 6",
            "front",
            "back",
            "clear",
            "size",
            "back",
        ]
        self.assertEqual(
            process_deque(test_cmd), ["ok", "ok", "ok", 2, 6, "ok", 0, "error"]
        )

    def test_case_2(self):
        test_cmd = ["pop_front", "back", "push_back 2", "size"]
        self.assertEqual(process_deque(test_cmd), ["error", "error", "ok", 1])

    def test_case_3(self):
        test_cmd = [
            "push_back 1",
            "push_front 10",
            "push_front 4",
            "push_front 5",
            "back",
            "pop_back",
            "pop_back",
            "back",
        ]
        self.assertEqual(process_deque(test_cmd), ["ok", "ok", "ok", "ok", 1, 1, 10, 4])

    def test_case_4(self):
        test_cmd = [
            "push_back 1",
            "push_back 2",
            "push_front 3",
            "push_back 4",
            "push_back 5",
            "push_front 6",
            "pop_back",
            "pop_back",
            "pop_front",
            "pop_back",
            "pop_front",
            "pop_front",
        ]
        self.assertEqual(
            process_deque(test_cmd),
            ["ok", "ok", "ok", "ok", "ok", "ok", 5, 4, 6, 2, 3, 1],
        )
