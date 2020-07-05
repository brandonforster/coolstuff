from api.model.node import Node


class Leaf(Node):
    right: 'Leaf'
    left: 'Leaf'

    def __init__(self, data):
        super().__init__(data)
