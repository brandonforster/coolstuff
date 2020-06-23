from typing import Set

from api.model.node import Node


class MultiLinkedNode(Node):
    def __init__(self, data, sinks: Set['MultiLinkedNode']):
        super().__init__(data)
        self.sinks = sinks

    def equals(self, other) -> bool:
        if self.data == other.data and self.sinks == other.sinks:
            return True
        return False
