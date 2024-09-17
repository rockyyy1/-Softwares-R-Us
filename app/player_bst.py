from __future__ import annotations
from typing import Optional

from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        """Initializes an empty binary tree"""
        self.root: PlayerBNode | None = None

    def insert(self, player : Player,
               _current_node: PlayerBNode | None = None) -> None:
        """Inserts a player into a binary search tree"""

        # create a new node of the player
        if self.root is None:
            self.root = PlayerBNode(player)
            return

        current_node = _current_node or self.root

        if player.player_name < current_node.player:
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
            else:
                self.insert(player, current_node.left)
        elif player.player_name > current_node.player:
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
            else:
                self.insert(player, current_node.right)
        else:
            print(f"Player '{player.player_name}' already exists.")
            current_node.player = player