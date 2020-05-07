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

    def test_reverse(self):
        one = Node("one")
        two = Node("two")
        three = Node("three")
        ll = linkedlist.LinkedList(one)
        ll.add(two)
        ll.add(three)

        ll = ll.reverse()

        expectedHead = three.data
        expectedMiddle = two.data
        expectedTail = one.data

        actualHead = ll.data
        actualMiddle = ll.next.data
        actualTail = ll.next.next.data

        self.assertEqual(expectedHead, actualHead)
        self.assertEqual(expectedMiddle, actualMiddle)
        self.assertEqual(expectedTail, actualTail)
