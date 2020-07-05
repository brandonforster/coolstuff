from typing import List

from api.model.leaf import Leaf


def bst(nums: List[int]) -> Leaf:
    nums.sort()

    head = Leaf(None)
    for num in nums:
        add_leaf(head, num)

    return head


def add_leaf(head: Leaf, data):
    if head.data is None:
        head.data = data
        return

    if data < head.data:
        if head.left is None:
            head.left = Leaf(None)
        add_leaf(head.left, data)

    if data > head.data:
        if head.right is None:
            head.right = Leaf(None)
        add_leaf(head.right, data)
