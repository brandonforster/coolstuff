from api.model.node import Node


class SinglyLinkedNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.next = None
