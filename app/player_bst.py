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
        if self.root is None:
            self.root = PlayerBNode(player)
            return

        current_node = _current_node or self.root

        if player.player_name.lower() < current_node.player.player_name.lower():
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
            else:
                self.insert(player, current_node.left)
        elif player.player_name.lower() > current_node.player.player_name.lower():
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
            else:
                self.insert(player, current_node.right)
        else:
            print(f"Player '{player.player_name}' already exists.")
            current_node.player = player

    def search(self, name : str, current_node : PlayerBNode | None = None) -> Player | None:
        """Searches for a player in the binary search tree"""
        if self.root is None:
            return None

        if current_node is None:
            current_node = self.root

        if current_node is None:
            return None

        name_lower = name.lower()
        current_name_lower = current_node.player.player_name.lower()

        if name_lower == current_name_lower:
            return current_node.player

        if name_lower < current_name_lower:
            if current_node.left is not None:
                return self.search(name, current_node.left)
            else:
                return None
        else:
            if current_node.right is not None:
                return self.search(name, current_node.right)
            else:
                return None