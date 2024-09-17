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

    def sort_list(self):
        """Creates a sorted list of PlayerBNode in Binary Search Tree"""
        sorted_list = []
        self.traverse(self.root, sorted_list)
        print(sorted_list)
        return sorted_list

    def traverse(self, node, sorted_list):
        """Recursively traverses a Binary Search Tree and adds nodes to a list"""
        if node is not None:
            self.traverse(node.left, sorted_list)
            sorted_list.append(node)
            self.traverse(node.right, sorted_list)

    def create_balanced_binary_search_tree(self) -> PlayerBNode:
        """Creates a balanced BST from a sorted list of PlayerBNodes"""
        sorted_list = self.sort_list()
        if not sorted_list:
            return None

        pivot = len(sorted_list) // 2
        mid_node = sorted_list[pivot]

        # Create a new node with the middle node
        new_root = PlayerBNode(mid_node.player)

        # Recursively create the left and right subtrees
        new_root.left = self.create_balanced_binary_search_tree(sorted_list[:pivot])
        new_root.right = self.create_balanced_binary_search_tree(sorted_list[pivot + 1:])

        return new_root


if __name__ == '__main__':
    player1 = Player("123","Rocky")
    bst = PlayerBST()
    bst.insert(player1)
    bst.create_balanced_binary_search_tree()




