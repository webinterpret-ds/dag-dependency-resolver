from dataclasses import (
    dataclass,
    field,
)
from typing import Text, List

from src.enums.node_status import NodeStatus


@dataclass
class Node:
    name: Text
    parents: List[str] = field(default_factory=list)
    status: NodeStatus = field(default=NodeStatus.NOT_VISITED)
