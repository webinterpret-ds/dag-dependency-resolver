import unittest

from src.graph import DependencyGraph
from src.node import Node


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.dependency_graph = DependencyGraph()

    def test_add_node(self):
        self.dependency_graph.add_node(name="test_node", parents=["a", "b"])
        assert self.dependency_graph.nodes == {"test_node": Node(name="test_node", parents=["a", "b"])}

    def test_get_dependencies_order(self):
        self.dependency_graph.add_node(name="a", parents=["b", "c"])
        self.dependency_graph.add_node(name="b", parents=[])
        self.dependency_graph.add_node(name="c", parents=[])

        dependencies_order = self.dependency_graph.get_dependencies_order()

        assert dependencies_order == ["b", "c", "a"]
