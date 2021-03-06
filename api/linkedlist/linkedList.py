from typing import Optional

from api.model.singlyLinkNode import SinglyLinkedNode


class LinkedList:
    def __init__(self, head: SinglyLinkedNode = None):
        self.head = head

    def get_head(self):
        return self.head

    def tail(self) -> SinglyLinkedNode:
        pointer = self.head

        while pointer.next is not None:
            pointer = pointer.next

        return pointer

    def add(self, new: SinglyLinkedNode) -> None:
        if self.head is None:
            self.head = new
            return

        tail = self.tail()
        new.next = None
        tail.next = new

    def delete(self, data) -> None:
        pointer = self.head

        while pointer.next.data is not data:
            pointer = pointer.next

        pointer.next = pointer.next.next

    def reverse(self):
        # no need to reverse if head is null
        # or there is only 1 node.
        if self.head is None or self.head.next is None:
            return self

        list_to_do = self.head.next

        reversed_list = self.head
        reversed_list.next = None

        while list_to_do is not None:
            temp = list_to_do
            list_to_do = list_to_do.next

            temp.next = reversed_list
            reversed_list = temp

        self.head = reversed_list
        return self

    def to_array(self):
        # shortcut for empty array
        if self.head is None:
            return []

        pointer = self.head
        array = [pointer.data]

        while pointer.next is not None:
            pointer = pointer.next
            array.append(pointer.data)

        return array

    def cycle_head(self) -> SinglyLinkedNode:
        traversed = {}

        cur = self.head
        while cur.next is not None:
            if traversed.get(cur.data):
                return cur

            traversed[cur.data] = True

            cur = cur.next

    def no_dupes(self):
        items = []
        cur = self.get_head()
        tail = None
        while cur is not None:
            if cur.data not in items:
                items.append(cur.data)
                tail = cur
            else:
                tail.next = cur.next

            cur = cur.next

    def is_palindrome(self):
        cur = self.head

        freq = {}

        while cur.next is not None:
            if cur.data in freq:
                freq[cur.data] += 1
            else:
                freq[cur.data] = 1
            cur = cur.next

        # palindromes must have exactly the same number of letters, except for potentially one letter.
        # init the letter count to the first letter in the dict
        count = freq[self.head.data]
        mismatch = False

        for f in freq.values():
            if f != count:
                # if there was already a mismatch, this is not a palindrome
                if mismatch:
                    return False
                else:
                    mismatch = True

        return True

    def intersection(self, other):
        cur = self.head

        nodes = {}

        while cur.next is not None:
            nodes[cur.data] = True
            cur = cur.next

        cur = other.head
        while cur.next is not None:
            if cur.data in nodes:
                return cur.data
            cur = cur.next

        return
