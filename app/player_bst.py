from __future__ import annotations
from typing import Optional


# node can be of any given type.
class Node[T]:
    def __init__(self, value: T) -> None:
        self.value = value
        self.left_node: Node[T] | None = None
        self.right_node: Optional[Node[T]] = None

    def __lt__(self, other: Node[T]) -> bool:
        if hasattr(other, 'value'):
            return self.value < other.value
        else:
            return self.value < other

    def __eq__(self, other: Node[T]) -> bool:
        if hasattr(other, 'value'):
            return self.value == other.value
        else:
            return self.value == other

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({self.value})'


class BST[T]:
    def __init__(self):
        self.root: Node[T] | None = None

    def insert(self, value: T,
               _current_node: Node | None = None):
        if _current_node and self.root is None:
            raise ValueError("Cannot insert")

        if not isinstance(_current_node, Node):
            raise TypeError("Not a Node")

        # create a new node of the value
        if self.root is None:
            self.root = Node(value)
            return
        current_node = _current_node or self.root

        if value < current_node:
            if current_node.left_node is None:
                current_node.left_node = Node(value)
                return
            self.insert(value, current_node.left_node)

        else:
            if current_node.right_node is None:
                current_node.right_node = Node(value)
                return
            self.insert(value, current_node.right_node)


bst = BST()
bst.insert(Node(1))
bst.insert(Node(2), Node(1))
