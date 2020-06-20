from abc import ABC


class Node(ABC):

    def __init__(self, data):
        self.data = data
        super().__init__()
