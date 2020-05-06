import node


class LinkedList:
    def __init__(self, head: node):
        self.head = head

    def tail(self):
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        return pointer

    def add(self, new: node):
        tail = self.tail()
        new.next = None
        tail.next = new

    def delete(self, data):
        pointer = self.head
        while pointer.next.data is not data:
            pointer = pointer.next
        pointer.next = pointer.next.next

    def reverse(self):
        return None
