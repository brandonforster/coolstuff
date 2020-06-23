import unittest

from api.graph.operations import find_route
from api.model.multiLinkedNode import MultiLinkedNode


class TestFindRoute(unittest.TestCase):
    def test_graph_with_route(self):
        end = MultiLinkedNode('end', set())
        middle = MultiLinkedNode('middle', {end})
        start = MultiLinkedNode('start', {middle})

        self.assertTrue(find_route(start, end))

    def test_graph_without_route(self):
        end = MultiLinkedNode('end', set())
        start = MultiLinkedNode('start', set())

        self.assertFalse(find_route(start, end))

    def test_graph_with_route_with_deadend(self):
        end = MultiLinkedNode('end', set())
        middle = MultiLinkedNode('middle', {end})
        deadend = MultiLinkedNode('deadend', set())
        start = MultiLinkedNode('start', {deadend, middle})

        self.assertTrue(find_route(start, end))


if __name__ == '__main__':
    unittest.main()
