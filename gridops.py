from typing import List


def rotate_image(img: List[List[int]]) -> List[List[int]]:
    for line in img:
        line.reverse()

    return img
