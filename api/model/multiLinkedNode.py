from typing import List

from api.model.node import Node


class MultiLinkedNode(Node):
    def __init__(self, data, sinks: List['MultiLinkedNode']):
        super().__init__(data)
        self.sinks = sinks
