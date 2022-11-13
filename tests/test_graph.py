import unittest

from src.graph import DependencyGraph
from src.node import Node


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.dependency_graph = DependencyGraph()

    def test_add_node(self) -> None:
        self.dependency_graph.add_node(name="c", parents=["a", "b"])

        self.assertDictEqual(self.dependency_graph.nodes, {"c": Node(name="c", parents=["a", "b"])})

    def test_get_dependencies_order(self) -> None:
        self.dependency_graph.add_node(name="a", parents=["b", "c"])
        self.dependency_graph.add_node(name="b", parents=[])
        self.dependency_graph.add_node(name="c", parents=[])

        dependencies_order = self.dependency_graph.get_dependencies_order()

        self.assertListEqual(dependencies_order, ["b", "c", "a"])

    def test_get_dependencies_order_disconnected_graph(self) -> None:
        self.dependency_graph.add_node(name="a", parents=[])
        self.dependency_graph.add_node(name="b", parents=[])
        self.dependency_graph.add_node(name="c", parents=[])

        dependencies_order = self.dependency_graph.get_dependencies_order()

        self.assertListEqual(dependencies_order, ["a", "b", "c"])
