from api.model.node import Node


class Leaf(Node):

    def __init__(self, data):
        super().__init__(data)
        self.left = None
        self.right = None

    def add_leaf(self, data) -> 'Leaf':
        if data < self.data:
            if self.left is None:
                self.left = Leaf(data)
                return self

            self.left.add_leaf(data)

        if data > self.data:
            if self.right is None:
                self.right = Leaf(data)
                return self

            self.right.add_leaf(data)

        return self
