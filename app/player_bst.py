from __future__ import annotations
from typing import Optional

from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self.root: PlayerBNode | None = None

    def insert(self, player : Player) -> None:
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

player1 = Player(uid = "001", player_name = "Bulbasaur")
bst = PlayerBST()
bst.insert(player1)
