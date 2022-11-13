from dataclasses import (
    dataclass,
    field,
)

from src.enums.node_status import NodeStatus


@dataclass
class Node:
    name: str
    parents: list = field(default_factory=list)
    status: NodeStatus = field(default=NodeStatus.NOT_VISITED)
