from api.model import multiLinkedNode


# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
def find_route(start: multiLinkedNode, end: multiLinkedNode) -> bool:
    if start.equals(end):
        return True

    for node in start.sinks:
        if find_route(node, end):
            return True

    return False
