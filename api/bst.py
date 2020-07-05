from typing import List

from api.model.leaf import Leaf


def bst(nums: List[int]) -> Leaf:
    nums.sort()

    iternums = iter(nums)
    head = Leaf(next(iternums))

    for num in iternums:
        head.add_leaf(num)

    return head
