import unittest

import linkedlist
from node import Node


class TestLinkedList(unittest.TestCase):
    def test_add(self):
        one = Node("one")
        two = Node("two")
        ll = linkedlist.LinkedList(one)
        ll.add(two)
        self.assertEqual(one.data, ll.head.data)
        self.assertEqual(two.data, ll.head.next.data)

    def test_delete(self):
        one = Node("one")
        two = Node("two")
        three = Node("three")
        ll = linkedlist.LinkedList(one)
        ll.add(two)
        ll.add(three)
        ll.delete("two")
        self.assertEqual(one.data, ll.head.data)
        self.assertEqual(three.data, ll.head.next.data)

    def test_tail(self):
        one = Node("one")
        two = Node("two")
        three = Node("three")
        ll = linkedlist.LinkedList(one)
        ll.add(two)
        ll.add(three)
        self.assertEqual(three.data, ll.tail().data)

    def test_reverse(self):
        one = Node("one")
        two = Node("two")
        three = Node("three")
        ll = linkedlist.LinkedList(one)
        ll.add(two)
        ll.add(three)
        ll = ll.reverse()
        self.assertEqual(three.data, ll.data)
        self.assertEqual(two.data, ll.next.data)
        self.assertEqual(one.data, ll.next.next.data)
