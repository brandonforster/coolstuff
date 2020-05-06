import node


class LinkedList:
    def __init__(self, head: node):
        self.cur = head
        self.last = None

    def add(self, new: node):
        self.last = self.cur
        self.cur = new

    def remove(self):
        self.cur = self.last
        self.last = None

    def reverse(self):
        return None
