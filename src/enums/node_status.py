from enum import (
    Enum,
    auto,
)


class NodeStatus(Enum):
    VISITED = auto()
    NOT_VISITED = auto()
