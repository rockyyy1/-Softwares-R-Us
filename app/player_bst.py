from __future__ import annotations
from typing import Optional

from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self.root: PlayerBNode | None = None

    def insert(self, player : Player,
               _current_node: PlayerBNode | None = None):

        if _current_node and self.root is None:
            raise ValueError("Cannot insert")

        if not isinstance(_current_node, PlayerBNode):
            raise TypeError("Not a PlayerBNode")

        # create a new node of the player
        if self.root is None:
            self.root = PlayerBNode(player)
            return

        current_node = _current_node or self.root

        if player.player_name < current_node.player.player_name:
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
                return
            self.insert(player, current_node.left)

        else:
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
                return
            self.insert(player, current_node.right)


player1 = Player(uid = "001", player_name = "Bulbasaur")
bst = PlayerBST()
bst.insert(player1)
