import json

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
        # no need to reverse if head is null
        # or there is only 1 node.
        if self.head is None or self.head.next is None:
            return self.head

        list_to_do = self.head.next

        reversed_list = self.head
        reversed_list.next = None

        while list_to_do is not None:
            temp = list_to_do
            list_to_do = list_to_do.next

            temp.next = reversed_list
            reversed_list = temp

        return reversed_list

    def to_array(self):
        pointer = self.head
        array = [pointer.data]

        while pointer.next is not None:
            pointer = pointer.next
            array.append(pointer.data)

        return array


class LinkedListEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, LinkedList):
            return {
                "_type": "linkedlist",
                "value": obj.to_array()
            }
        return super(LinkedListEncoder, self).default(obj)
