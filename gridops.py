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
    width = len(grid[0])
    height = len(grid)

    # find all zeroes
    zero_x_map = {}
    zero_y_map = {}
    for x in range(0, width):
        for y in range(0, height):
            if grid[x][y] == 0:
                zero_x_map[x] = True
                zero_y_map[y] = True
            else:
                if x not in zero_x_map:
                    zero_x_map[x] = False
                if y not in zero_y_map:
                    zero_y_map[y] = False

    # zero out
    for x in range(0, width):
        for y in range(0, height):
            if zero_x_map[x] or zero_y_map[y]:
                grid[x][y] = 0

    return grid
