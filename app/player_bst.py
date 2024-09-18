from __future__ import annotations

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

        if player.player_name.lower() == current_node.player.player_name.lower():
            print(f"Updated '{player.player_name}'")
            current_node.player = player
            return
        elif player.player_name.lower() < current_node.player.player_name.lower():
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
            else:
                self.insert(player, current_node.left)
        elif player.player_name.lower() > current_node.player.player_name.lower():
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
            else:
                self.insert(player, current_node.right)

    def search(self, name : str, current_node : PlayerBNode | None = None) -> Player | None:
        """Searches for a player in the binary search tree"""
        if self.root is None:
            return None

        if current_node is None:
            current_node = self.root

        name = name.lower()

        if name == current_node.player.player_name.lower():
            return current_node.player

        if name < current_node.player.player_name.lower():
            if current_node.left is not None:
                return self.search(name, current_node.left)
            else:
                return None
        else:
            if current_node.right is not None:
                return self.search(name, current_node.right)
            else:
                return None

    def sort_nodes_to_list(self) -> list[PlayerBNode]:
        """Creates a sorted list of PlayerBNode in Binary Search Tree"""
        def traverse(node) -> list[PlayerBNode]:
            """Recursively traverses a Binary Search Tree and adds nodes to a list"""
            if node is None:
                return []

            return traverse(node.left) + [node] + traverse(node.right)

        return traverse(self.root)

def create_balanced_bst(sorted_list: list[PlayerBNode]) -> PlayerBST | None:
    """Creates a balanced BST from a sorted list of PlayerBNodes"""
    if len(sorted_list) == 0:
        return None

    def assign_middle(sorted_nodes: list[PlayerBNode]) -> PlayerBNode | None:
        """Recursively assigns left/right of the root node"""
        if len(sorted_nodes) == 0:
            return None

        middle_element = len(sorted_nodes) // 2

        middle_node = sorted_nodes[middle_element]
        middle_node.left = assign_middle(sorted_nodes[:middle_element])
        middle_node.right = assign_middle(sorted_nodes[middle_element + 1:])

        return middle_node

    bst_root = assign_middle(sorted_list)
    new_bst = PlayerBST()
    new_bst.root = bst_root

    return new_bst
