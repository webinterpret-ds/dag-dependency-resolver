from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Dict,
    List,
    Text,
)

from src.enums.node_status import NodeStatus
from src.node import Node


@dataclass
class DependencyGraph:
    nodes: Dict[Text, Node] = field(default_factory=dict)

    def add_node(self, name: str, parents: List[Text]) -> None:
        self.nodes[name] = Node(name=name, parents=parents)

    def get_dependencies_order(self) -> List[str]:
        dependencies_order: List[str] = []

        for node in self.nodes.values():
            self._solve_deps(node, dependencies_order)

        self._reset_nodes_status()
        return dependencies_order

    def _solve_deps(self, node: Node, dependencies_order: List[Text]) -> None:
        if node.status != NodeStatus.VISITED:
            for parent in node.parents:
                self._solve_deps(self.nodes[parent], dependencies_order)

            node.status = NodeStatus.VISITED

            dependencies_order.append(node.name)

    def _reset_nodes_status(self) -> None:
        for node in self.nodes.values():
            node.status = NodeStatus.UNVISITED
