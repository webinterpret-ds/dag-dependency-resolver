from enum import (
    Enum,
    auto,
)


class NodeStatus(Enum):
    VISITED = auto()
    UNVISITED = auto()
