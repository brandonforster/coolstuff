from typing import List


def rotate_image(img: List[List[int]]) -> List[List[int]]:
    width = len(img[0])
    height = len(img)

    rotated = [[0 for x in range(width)] for y in range(height)]

    for x in range(0, width):
        for y in range(0, height):
            rotated[x][y] = img[y][x]
        rotated[x].reverse()

    return rotated


def zero_out(grid: List[List[int]]) -> List[List[int]]:
    return grid
