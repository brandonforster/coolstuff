import unittest

import linkedlist
from node import Node


class TestLinkedList(unittest.TestCase):
    def test_Add(self):
        one = Node("one")
        two = Node("two")
        ll = linkedlist.LinkedList(one)
        ll.add(two)
        self.assertEqual(ll.last,one)
        self.assertEqual(ll.cur,two)
