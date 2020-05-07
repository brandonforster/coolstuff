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

    def test_add_no_head(self):
        one = Node("one")
        ll = linkedlist.LinkedList()

        ll.add(one)

        self.assertEqual(one.data, ll.head.data)

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

        actual = ll.tail().data

        self.assertEqual(three.data, actual)

    def test_array(self):
        one = Node("one")
        two = Node("two")
        three = Node("three")
        ll = linkedlist.LinkedList(one)
        ll.add(two)
        ll.add(three)

        expected = ["one", "two", "three"]

        actual = ll.to_array()

        self.assertEqual(expected, actual)

    def test_array_empty(self):
        ll = linkedlist.LinkedList()

        expected = []

        actual = ll.to_array()

        self.assertEqual(expected, actual)

    def test_reverse(self):
        one = Node("one")
        two = Node("two")
        three = Node("three")
        ll = linkedlist.LinkedList(one)
        ll.add(two)
        ll.add(three)

        ll = ll.reverse()

        expected_head = three.data
        expected_middle = two.data
        expected_tail = one.data

        actual_head = ll.head.data
        actual_middle = ll.head.next.data
        actual_tail = ll.head.next.next.data

        self.assertEqual(expected_head, actual_head)
        self.assertEqual(expected_middle, actual_middle)
        self.assertEqual(expected_tail, actual_tail)
