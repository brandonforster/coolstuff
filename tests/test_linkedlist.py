import unittest

from api.model.singlyLinkNode import SinglyLinkedNode
from api.linkedlist.linkedList import LinkedList
from api.server import api


class TestLinkedList(unittest.TestCase):
    def test_add(self):
        one = SinglyLinkedNode("one")
        two = SinglyLinkedNode("two")
        ll = LinkedList(one)

        ll.add(two)

        self.assertEqual(one.data, ll.head.data)
        self.assertEqual(two.data, ll.head.next.data)

    def test_add_no_head(self):
        one = SinglyLinkedNode("one")
        ll = LinkedList()

        ll.add(one)

        self.assertEqual(one.data, ll.head.data)

    def test_delete(self):
        one = SinglyLinkedNode("one")
        two = SinglyLinkedNode("two")
        three = SinglyLinkedNode("three")
        ll = LinkedList(one)
        ll.add(two)
        ll.add(three)

        ll.delete("two")

        self.assertEqual(one.data, ll.head.data)
        self.assertEqual(three.data, ll.head.next.data)

    def test_tail(self):
        one = SinglyLinkedNode("one")
        two = SinglyLinkedNode("two")
        three = SinglyLinkedNode("three")
        ll = LinkedList(one)
        ll.add(two)
        ll.add(three)

        actual = ll.tail().data

        self.assertEqual(three.data, actual)

    def test_array(self):
        one = SinglyLinkedNode("one")
        two = SinglyLinkedNode("two")
        three = SinglyLinkedNode("three")
        ll = LinkedList(one)
        ll.add(two)
        ll.add(three)

        expected = ["one", "two", "three"]

        actual = ll.to_array()

        self.assertEqual(expected, actual)

    def test_array_empty(self):
        ll = LinkedList()

        expected = []

        actual = ll.to_array()

        self.assertEqual(expected, actual)

    def test_reverse(self):
        one = SinglyLinkedNode("one")
        two = SinglyLinkedNode("two")
        three = SinglyLinkedNode("three")
        ll = LinkedList(one)
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

    def test_cycle(self):
        alpha = SinglyLinkedNode("A")
        bravo = SinglyLinkedNode("B")
        charlie = SinglyLinkedNode("C")
        delta = SinglyLinkedNode("D")
        echo = SinglyLinkedNode("E")

        ll = LinkedList(alpha)
        ll.add(bravo)
        ll.add(charlie)
        ll.add(delta)

        echo.next = charlie
        delta.next = echo

        expected_cycle_head = charlie

        self.assertEqual(expected_cycle_head, ll.cycle_head())


if __name__ == '__main__':
    unittest.main()
