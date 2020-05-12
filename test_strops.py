import unittest

from strops import is_unique


class TestIsUnique(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(is_unique(""))

    def test_unique(self):
        self.assertTrue(is_unique("unique"))

    def test_not_unique(self):
        self.assertFalse(is_unique("racecar"))
