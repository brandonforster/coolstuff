import unittest

from gridops import rotate_image


class TestGridOps(unittest.TestCase):
    def test_rotate(self):
        start_img = [[1, 0, 0, 1],
                     [1, 0, 0, 1],
                     [1, 0, 0, 1],
                     [1, 0, 0, 1]]

        expect_img = [[1, 1, 1, 1],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [1, 1, 1, 1]]

        actual_img = rotate_image(start_img)

        self.assertEqual(expect_img, actual_img)

    def test_rotate_stack_overflow(self):
        start_img = [[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 0, 1, 2],
                     [3, 4, 5, 6]]

        expect_img = [[3, 9, 5, 1],
                      [4, 0, 6, 2],
                      [5, 1, 7, 3],
                      [6, 2, 8, 4]]

        actual_img = rotate_image(start_img)

        self.assertEqual(expect_img, actual_img)

    def test_zero_out(self):
        start_grid = [[1, 1, 0, 1],
                      [1, 1, 1, 1],
                      [1, 0, 1, 1],
                      [1, 1, 1, 1]]

        expect_grid = [[0, 0, 0, 0],
                       [1, 0, 0, 1],
                       [0, 0, 0, 0],
                       [1, 0, 0, 1]]

        actual_grid = rotate_image(start_grid)

        self.assertEqual(expect_grid, actual_grid)
