import unittest

from api.bst import bst


class TestNewBST(unittest.TestCase):
    def test_bst(self):
        some_ints = [2, 4, 1, 8, 10, 15, 9, 12, 42]

        head = bst(some_ints)

        self.assertTrue(head, True)


if __name__ == '__main__':
    unittest.main()
