import time
import unittest

from strops import is_unique, is_unique_slow, is_palindrome


class TestIsStringOps(unittest.TestCase):
    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 10)))

    def test_empty(self):
        self.assertTrue(is_unique(""))

    def test_unique(self):
        self.assertTrue(is_unique("honda"))

    def test_not_unique(self):
        self.assertFalse(is_unique("snakes"))

    def test_empty_slow(self):
        self.assertTrue(is_unique_slow(""))

    def test_unique_slow(self):
        self.assertTrue(is_unique_slow("honda"))

    def test_not_unique_slow(self):
        self.assertFalse(is_unique_slow("snakes"))

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("tacocat"))

    def test_is_palindrome_true_order(self):
        self.assertTrue(is_palindrome("ttaacco"))

    def test_is_palindrome_true_symbols(self):
        self.assertTrue(is_palindrome("!=+=!"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("taco cat"))
