import unittest
from typing import List

from gridops import rotate_image


class TestGridOps(unittest.TestCase):
    def test_rotate(self):
        start_img = [[1, 1, 0],
                     [1, 0, 1],
                     [0, 1, 1]]

        expect_img = [[0, 1, 1],
                      [1, 0, 1],
                      [1, 1, 0]]

        actual_img = rotate_image(start_img)

        self.assertEqual(expect_img, actual_img)
