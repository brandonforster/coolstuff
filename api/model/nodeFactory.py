from api.model.multiLinkedNode import MultiLinkedNode
from api.model.node import Node
from api.model.singlyLinkNode import SinglyLinkedNode


def node_factory(data, sink) -> Node:
    if isinstance(sink, list):
        return MultiLinkedNode(data, sink)

    sln = SinglyLinkedNode(data)
    sln.next = sink
    return sln
