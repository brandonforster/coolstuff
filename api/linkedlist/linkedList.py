from api.model.singlyLinkNode import SinglyLinkedNode


class LinkedList:
    def __init__(self, head: SinglyLinkedNode = None):
        self.head = head

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

