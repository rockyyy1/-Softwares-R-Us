from __future__ import annotations
from typing import Optional

from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self.root: PlayerBNode | None = None

    def insert(self, player : Player) -> None:
        # create a new node of the player
        if self.root is None:
            self.root = PlayerBNode(player)
            return

        current_node = self.root

        # left subtree
        if player.player_name < current_node.player.player_name:
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
                return
            self.insert(current_node.player)

        # right subtree
        else:
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
                return
            self.insert(current_node.player)



player1 = Player(uid = "001", player_name = "Bulbasaur")
bst = PlayerBST()
bst.insert(player1)
