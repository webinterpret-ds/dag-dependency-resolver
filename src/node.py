from dataclasses import (
    dataclass,
    field,
)
from typing import (
    List,
    Text,
)

from src.enums.node_status import NodeStatus


@dataclass
class Node:
    name: Text
    parents: List[Text] = field(default_factory=list)
    status: NodeStatus = field(default=NodeStatus.UNVISITED)
